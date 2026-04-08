# TypeScript Conventions

> Applied to all `*.ts` and `*.tsx` files.

## Naming

| Item | Case | Example |
|------|------|---------|
| Interfaces, Types, Classes, Components | PascalCase | `UserProfile`, `AuthService` |
| Functions, Variables, Methods | camelCase | `getUser`, `isActive` |
| Constants | SCREAMING_SNAKE_CASE | `MAX_RETRY_COUNT` |
| File names | kebab-case | `user-profile.ts` |
| Enum values | PascalCase | `Status.Active` |

## Type Safety

```typescript
// ❌ NEVER
const data: any = fetchData()
// @ts-ignore
brokenCall()

// ✅ ALWAYS
const data: unknown = fetchData()
if (isUserData(data)) { /* now typed */ }
```

### Rules
- NO `any` without explicit justification comment
- NO `@ts-ignore` or `@ts-expect-error` without explanation
- Prefer `unknown` over `any` when type is truly unknown
- Use explicit return types on exported functions
- Use discriminated unions over type assertions

## Imports

```typescript
// 1. External packages
import { NextRequest } from 'next/server'
import { z } from 'zod'

// 2. Internal modules (absolute paths)
import { AuthService } from '@/services/auth'
import { UserSchema } from '@/schemas/user'

// 3. Relative
import { UserCard } from './user-card'
import type { UserProps } from './types'
```

### Rules
- Group: external → internal → relative
- Use named exports over default exports
- No circular dependencies
- Use `type` imports for type-only imports

## Async/Await

```typescript
// ❌ Floating promise
fetchUser(id)

// ❌ Silent failure
try { await riskyOp() } catch(e) {}

// ✅ Handled
try {
  const user = await fetchUser(id)
  return user
} catch (error) {
  logger.error('Failed to fetch user', { id, error })
  throw new AppError('USER_FETCH_FAILED', { cause: error })
}
```

### Rules
- Always handle promise rejections
- Use try/catch for async operations
- Avoid floating promises (unhandled)
- Use `Promise.all()` for independent parallel operations

## Functions

```typescript
// ❌ Too broad
function processData(data: any): any { ... }

// ✅ Explicit
function processUser(user: RawUserData): ProcessedUser { ... }
```

### Rules
- Explicit return types on exported functions
- Single responsibility — one function, one job
- Max 3 parameters — use an options object for more
- Early returns over deep nesting

## Error Handling

```typescript
// ❌ Generic error
throw new Error('something went wrong')

// ✅ Typed error with context
throw new AppError('INVALID_CREDENTIALS', {
  statusCode: 401,
  context: { email: user.email },
})
```

### Rules
- Use typed errors with error codes
- Include context in error messages
- Never swallow errors with empty catch blocks
- Log errors at the boundary, not at every level
