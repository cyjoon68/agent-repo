# Software Requirements Specification (SRS) Template

## Document Structure

```markdown
# Software Requirements Specification
## [Project Name]

### 1. Introduction
#### 1.1 Purpose
#### 1.2 Scope
#### 1.3 Definitions, Acronyms, and Abbreviations
#### 1.4 References
#### 1.5 Overview

### 2. Overall Description
#### 2.1 Product Perspective
#### 2.2 Product Functions
#### 2.3 User Characteristics
#### 2.4 Constraints
#### 2.5 Assumptions and Dependencies

### 3. Specific Requirements
#### 3.1 Functional Requirements
##### FR-001: [Requirement Name]
- Description:
- Priority: High/Medium/Low
- Input:
- Output:
- Acceptance Criteria:

#### 3.2 Non-Functional Requirements
##### NFR-001: [Requirement Name]
- Category: Performance/Security/Usability/Reliability
- Description:
- Metric:

### 4. Appendices
```

## Requirement Writing Guidelines

### Functional Requirement Format
- Use unique identifiers (FR-001, FR-002)
- State requirements using "shall" for mandatory, "should" for optional
- Include acceptance criteria for each requirement
- Specify priority level

### Non-Functional Requirement Categories
- **Performance**: Response time, throughput, resource usage
- **Security**: Authentication, authorization, data protection
- **Usability**: Accessibility, user experience
- **Reliability**: Availability, fault tolerance, recovery

## Example

```markdown
##### FR-001: User Login
- Description: The system shall authenticate users via email and password
- Priority: High
- Input: Email address, password
- Output: Authentication token or error message
- Acceptance Criteria:
  - Valid credentials return JWT token within 2 seconds
  - Invalid credentials display appropriate error message
  - Account locks after 5 failed attempts
```
