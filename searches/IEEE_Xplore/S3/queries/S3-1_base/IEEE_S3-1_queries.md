# IEEE Xplore S3-1 — Base query variants

### S3-1A — 2 result(s)
```text
(
  "All Metadata":"dynamic building stock model*" OR
  "All Metadata":"dynamic building stock modelling" OR
  "All Metadata":"building stock dynamic model*" OR
  "All Metadata":"building stock turnover dynamic*" OR
  "All Metadata":"stock turnover dynamic*" OR
  "All Metadata":"building stock mortality" OR
  "All Metadata":"building stock survival"
)
```

### S3-1B-part1 — 1 result(s)
```text
(
  (
    "All Metadata":"building stock*" OR
    "All Metadata":"urban building stock*" OR
    "All Metadata":"residential building stock*" OR
    "All Metadata":"urban residential building*"
  )
  AND
  (
    "All Metadata":"building lifetime*" OR
    "All Metadata":"building lifespan*" OR
    "All Metadata":"service life distribution*" OR
    "All Metadata":"lifetime distribution*" OR
    "All Metadata":"demolition rate*" OR
    "All Metadata":"demolition probabilit*"
  )
)
```

### S3-1B-part2 — 0 result(s)
```text
(
  (
    "All Metadata":"building stock*" OR
    "All Metadata":"urban building stock*" OR
    "All Metadata":"residential building stock*" OR
    "All Metadata":"urban residential building*"
  )
  AND
  (
    "All Metadata":"demolition timing" OR
    "All Metadata":"demolition record*" OR
    "All Metadata":"demolition data"
  )
)
```

### S3-1C — 0 result(s)
```text
(
  "All Metadata":building*
  AND
  (
    "All Metadata":"service life distribution*" OR
    "All Metadata":"lifetime distribution*"
  )
  AND
  (
    "All Metadata":"demolition record*" OR
    "All Metadata":"demolition data" OR
    "All Metadata":"demolition big data"
  )
)
```

### S3-1D — 0 result(s)
```text
(
  "All Metadata":"building lifespan assumption*" OR
  "All Metadata":"building lifetime assumption*"
)
```

### S3-1E — 0 result(s)
```text
(
  (
    "All Metadata":"material stock*" OR
    "All Metadata":"building material stock*"
  )
  AND
  (
    "All Metadata":"building lifespan*" OR
    "All Metadata":"building lifetime*"
  )
  AND
  (
    "All Metadata":"demolition waste" OR
    "All Metadata":outflow* OR
    "All Metadata":"material flow*"
  )
)
```

### S3-1F — 1 result(s)
```text
(
  (
    "All Metadata":"building stock*" OR
    "All Metadata":"building stocks"
  )
  AND
  (
    "All Metadata":"construction material flow*" OR
    "All Metadata":"material flow*" OR
    "All Metadata":"material outflow*" OR
    "All Metadata":"stock outflow*"
  )
  AND
  (
    "All Metadata":temporal OR
    "All Metadata":dynamic* OR
    "All Metadata":prospective OR
    "All Metadata":"over time" OR
    "All Metadata":"space and time"
  )
)
```

### S3-1G — 0 result(s)
```text
(
  "All Metadata":building*
  AND
  (
    "All Metadata":"stock turnover dynamics" OR
    "All Metadata":"building stock turnover"
  )
)
```
