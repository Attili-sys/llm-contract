# llm-contracts Validation Report

**Generated**: 2025-07-20 20:13:33
**Schema**: `/var/folders/xn/bb6_zgm968sdjb_lgckkqvk00000gp/T/tmp_3xv6vtx.yaml`

## Summary

- **Status**: ❌ FAILED
- **Errors**: 1
- **Success Rate**: 0.0%

## Test Results

### ❌ Validation Failed

Found 1 validation error(s):

#### Content Rules

- Word count (43) below minimum (50)

## Schema Reference

### Rules Applied

**Rule 1**:
```yaml
{'keyword_must_include': ['quality', 'premium']}
```

**Rule 2**:
```yaml
{'keyword_must_not_include': ['cheap', 'low quality']}
```

**Rule 3**:
```yaml
{'word_count_min': 50}
```

**Rule 4**:
```yaml
{'keyword_must_include': 'warranty'}
```

**Rule 5**:
```yaml
{'phrase_proximity': {'max_distance': 20, 'terms': ['warranty', '30']}}
```
