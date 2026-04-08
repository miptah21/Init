# Testing Conventions

> Applied to all `*.test.ts`, `*.spec.ts`, and `__tests__/` files.

## Structure

Use BDD-style comments to clearly separate test phases:

```typescript
describe('UserService', () => {
  describe('getUser', () => {
    it('should return user when found', async () => {
      // #given
      const mockUser = { id: '1', name: 'Test User' }
      mockDb.findById.mockResolvedValue(mockUser)

      // #when
      const result = await userService.getUser('1')

      // #then
      expect(result).toEqual(mockUser)
    })

    it('should throw NotFoundError when user does not exist', async () => {
      // #given
      mockDb.findById.mockResolvedValue(null)

      // #when & #then
      await expect(userService.getUser('999'))
        .rejects.toThrow(NotFoundError)
    })
  })
})
```

## Rules

### Test Organization
- One logical assertion per test
- Descriptive test names that explain the scenario and expected outcome
- Group related tests with nested `describe` blocks
- Name the describe block after the unit under test

### Mocking
- Mock external dependencies (APIs, databases, file system)
- **Never** mock the unit under test
- Reset mocks between tests (`beforeEach` / `afterEach`)
- Prefer dependency injection over module mocking

### Coverage Requirements
- Test happy path AND error cases
- Test edge cases: empty arrays, null values, boundary values
- Test async behavior: loading, success, error states
- Auth/payments paths require thorough coverage

### Anti-Patterns

| ❌ Don't | ✅ Do Instead |
|----------|--------------|
| Test implementation details | Test behavior and output |
| Share mutable state between tests | Reset state in `beforeEach` |
| Use magic numbers/strings | Use descriptive constants |
| Write overly long test names | Be concise but descriptive |
| Delete failing tests to "pass" | Fix the code or update the test |
| Use `test.skip` without a reason | Add a TODO comment explaining why |

### Test File Naming

```
src/
  services/
    user-service.ts
    user-service.test.ts        # Co-located unit test
  __tests__/
    integration/
      user-api.test.ts          # Integration tests
```

### Snapshot Testing
- Use sparingly — only for stable UI components
- Review snapshot changes carefully in PRs
- Never auto-update snapshots without understanding changes
