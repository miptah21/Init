# React & Next.js Best Practices

> Performance optimization guidelines adapted from Vercel Engineering.
> 45 rules across 8 categories, prioritized by impact.

---

## Priority 1: Eliminating Waterfalls (CRITICAL)

### Defer await to where it's used
```typescript
// ❌ Blocks everything
async function Page() {
  const user = await getUser()     // waits here
  const posts = await getPosts()   // then waits here
  return <Dashboard user={user} posts={posts} />
}

// ✅ Parallel
async function Page() {
  const userPromise = getUser()
  const postsPromise = getPosts()
  const [user, posts] = await Promise.all([userPromise, postsPromise])
  return <Dashboard user={user} posts={posts} />
}
```

### Use Suspense boundaries for streaming
```tsx
// ✅ Stream independent parts
export default function Page() {
  return (
    <main>
      <Header />
      <Suspense fallback={<PostsSkeleton />}>
        <Posts />
      </Suspense>
      <Suspense fallback={<CommentsSkeleton />}>
        <Comments />
      </Suspense>
    </main>
  )
}
```

---

## Priority 2: Bundle Size (CRITICAL)

### Import directly, avoid barrel files
```typescript
// ❌ Pulls entire library
import { Button } from '@/components'

// ✅ Direct import
import { Button } from '@/components/ui/button'
```

### Dynamic imports for heavy components
```typescript
// ✅ Code split
const HeavyChart = dynamic(() => import('@/components/chart'), {
  loading: () => <ChartSkeleton />,
  ssr: false,
})
```

### Defer third-party scripts
```typescript
// ✅ Load analytics after hydration
import Script from 'next/script'
<Script src="https://analytics.example.com/script.js" strategy="lazyOnload" />
```

---

## Priority 3: Server-Side Performance (HIGH)

### Use React.cache() for per-request dedup
```typescript
import { cache } from 'react'

export const getUser = cache(async (id: string) => {
  return db.user.findUnique({ where: { id } })
})

// Called multiple times in component tree → only 1 DB query
```

### Minimize data passed to client components
```typescript
// ❌ Sends full object
<ClientComponent data={fullUserObject} />

// ✅ Send only what's needed
<ClientComponent name={user.name} avatar={user.avatar} />
```

### Use after() for non-blocking operations
```typescript
import { after } from 'next/server'

export async function POST(req: Request) {
  const result = await processOrder(req)

  after(async () => {
    await sendConfirmationEmail(result.orderId)
    await updateAnalytics(result)
  })

  return Response.json(result)
}
```

---

## Priority 4: Re-render Optimization (MEDIUM)

### Don't subscribe to state only used in callbacks
```typescript
// ❌ Re-renders on every count change
function Component() {
  const count = useStore(state => state.count)
  const onClick = () => sendAnalytics(count)
}

// ✅ Read in callback
function Component() {
  const onClick = () => {
    const count = useStore.getState().count
    sendAnalytics(count)
  }
}
```

### Use useMemo for expensive calculations
```typescript
// ❌ useEffect + setState
const [filtered, setFiltered] = useState([])
useEffect(() => {
  setFiltered(items.filter(expensiveFilter))
}, [items])

// ✅ useMemo
const filtered = useMemo(
  () => items.filter(expensiveFilter),
  [items]
)
```

### Use key prop to reset component state
```typescript
// ❌ useEffect to reset
useEffect(() => {
  setInput('')
}, [userId])

// ✅ Key prop
<EditForm key={userId} />
```

---

## Priority 5: useEffect Best Practices

### When you DON'T need useEffect

| Situation | Don't | Do Instead |
|-----------|-------|-----------|
| Derived state | `useState` + `useEffect` | Calculate during render |
| Expensive calc | `useEffect` cache | `useMemo` |
| Reset on prop change | `useEffect` + `setState` | `key` prop |
| User events | `useEffect` watching state | Event handler |
| Notify parent | `useEffect` calling onChange | Call in event handler |

### When you DO need useEffect
- Synchronizing with **external systems** (non-React widgets, browser APIs)
- **Subscriptions** to external stores
- **Data fetching** with proper cleanup (or use framework's mechanism)

### Decision tree
```
Need to respond to something?
├── User interaction? → EVENT HANDLER
├── Component appeared? → EFFECT (external sync, analytics)
├── Props changed, need derived value? → CALCULATE DURING RENDER
│   └── Expensive? → useMemo
└── Reset state on prop change? → KEY PROP
```

---

## Priority 6: JavaScript Performance (LOW-MEDIUM)

### Quick wins
- Use `Set`/`Map` for O(1) lookups instead of `Array.includes()`
- Combine `.filter().map()` into single `.reduce()` or loop
- Check `.length` before expensive array comparisons
- Return early from functions
- Cache `localStorage`/`sessionStorage` reads
- Hoist RegExp creation outside loops

---

## Quick Reference Checklist

```
Before shipping, verify:
□ No sequential awaits that could be parallel
□ No barrel file imports pulling unused code
□ Heavy components use dynamic()
□ Server components don't pass unnecessary data to client
□ No useEffect for derived state
□ No useEffect + setState for prop-based reset (use key)
□ Expensive calculations use useMemo
□ Lists have stable, unique keys
□ Images use next/image
□ Third-party scripts deferred with next/script
```
