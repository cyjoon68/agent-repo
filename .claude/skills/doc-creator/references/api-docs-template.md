# API Documentation Template

## Document Structure

```markdown
# [API Name] API Documentation

## Overview
Brief description of the API purpose and capabilities.

## Base URL
`https://api.example.com/v1`

## Authentication
Describe authentication method (API Key, OAuth, JWT, etc.)

## Endpoints

### [Resource Name]

#### GET /resource
Description of what this endpoint does.

**Parameters**
| Name | Type | Required | Description |
|------|------|----------|-------------|
| id   | string | Yes | Resource identifier |

**Response**
```json
{
  "id": "123",
  "name": "Example"
}
```

**Status Codes**
| Code | Description |
|------|-------------|
| 200  | Success |
| 404  | Not found |

## Error Handling
Standard error response format.

## Rate Limiting
API rate limit information.
```

## Function/Class Documentation Format

```markdown
## [Function/Class Name]

### Description
What this function/class does.

### Signature
`functionName(param1: Type, param2: Type): ReturnType`

### Parameters
| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| param1    | string | - | Description |

### Returns
Description of return value.

### Example
```typescript
const result = functionName("value", 123);
```

### Throws
- `ErrorType`: When condition occurs
```

## Best Practices

- Include working code examples
- Document all possible error responses
- Specify data types explicitly
- Add deprecation notices when applicable
- Include version information
