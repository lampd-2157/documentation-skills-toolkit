<!-- Template T12: Architecture Diagram — Copy this file and customize -->
<!-- sections:
  required: [Context Diagram, Component Diagram, Data Flow]
  recommended: [Technology Stack, Deployment View, Security Boundaries]
  optional: [Performance Considerations, Evolution Roadmap]
-->
# [System Name] — Architecture

!!! info "Document Metadata"
    | Field | Value |
    |-------|-------|
    | **Owner** | [team/person] |
    | **Status** | [draft/review/approved] |
    | **Last reviewed** | [YYYY-MM-DD] |
    | **Scope** | [what this diagram covers] |

## Context Diagram

High-level view: how the system interacts with users and external systems.

```mermaid
graph TB
    U[Users] -->|HTTPS| SYS[System Name]
    SYS -->|API| EXT1[External Service 1]
    SYS -->|Events| EXT2[Message Queue]
    ADM[Admin] -->|SSH/HTTPS| SYS
```

| Actor / System | Interaction | Protocol | Notes |
|----------------|-------------|----------|-------|
| Users | [what they do] | HTTPS | [notes] |
| External Service 1 | [integration type] | REST API | [notes] |
| Admin | [management access] | SSH/HTTPS | [notes] |

## Component Diagram

Internal components and how they communicate.

```mermaid
graph LR
    subgraph Frontend
        WEB[Web App]
        MOB[Mobile App]
    end
    subgraph Backend
        API[API Gateway]
        SVC1[Service A]
        SVC2[Service B]
        WORKER[Background Worker]
    end
    subgraph Data
        DB[(Database)]
        CACHE[(Cache)]
        QUEUE[Message Queue]
    end

    WEB & MOB --> API
    API --> SVC1 & SVC2
    SVC1 & SVC2 --> DB & CACHE
    SVC1 --> QUEUE --> WORKER
    WORKER --> DB
```

| Component | Responsibility | Technology | Owner |
|-----------|---------------|------------|-------|
| API Gateway | Request routing, auth | [tech] | [team] |
| Service A | [core domain logic] | [tech] | [team] |
| Service B | [secondary domain] | [tech] | [team] |
| Database | Persistent storage | [tech] | [team] |

## Data Flow

How data moves through the system for key operations.

```mermaid
sequenceDiagram
    participant U as User
    participant API as API Gateway
    participant SVC as Service
    participant DB as Database
    participant Q as Queue

    U->>API: Request
    API->>SVC: Validated request
    SVC->>DB: Read/Write
    DB-->>SVC: Result
    SVC->>Q: Async event
    SVC-->>API: Response
    API-->>U: Result
```

| Flow | Trigger | Path | SLA |
|------|---------|------|-----|
| [User action] | [event] | User → API → Service → DB | [latency target] |
| [Background job] | [schedule/event] | Queue → Worker → DB | [throughput target] |

## Technology Stack

| Layer | Technology | Version | Purpose |
|-------|-----------|---------|---------|
| Frontend | [framework] | [ver] | [why chosen] |
| Backend | [language/framework] | [ver] | [why chosen] |
| Database | [DB engine] | [ver] | [why chosen] |
| Cache | [cache engine] | [ver] | [why chosen] |
| Queue | [message broker] | [ver] | [why chosen] |
| Infrastructure | [cloud/on-prem] | — | [why chosen] |

## Deployment View

```mermaid
graph TB
    subgraph Production
        LB[Load Balancer]
        subgraph AZ-1
            APP1[App Server 1]
            DB1[(DB Primary)]
        end
        subgraph AZ-2
            APP2[App Server 2]
            DB2[(DB Replica)]
        end
    end
    LB --> APP1 & APP2
    DB1 -.->|replication| DB2
```

| Environment | Instances | Region/AZ | Notes |
|-------------|-----------|-----------|-------|
| Production | [count] | [region] | [HA setup] |
| Staging | [count] | [region] | [mirrors prod] |

## Security Boundaries

```mermaid
graph TB
    subgraph Public Zone
        CDN[CDN]
        LB[Load Balancer]
    end
    subgraph DMZ
        WAF[WAF]
        API[API Gateway]
    end
    subgraph Private Zone
        SVC[Services]
        DB[(Database)]
    end
    CDN --> LB --> WAF --> API --> SVC --> DB
```

| Boundary | Controls | Notes |
|----------|----------|-------|
| Public → DMZ | WAF, rate limiting, TLS | [details] |
| DMZ → Private | Network ACL, auth tokens | [details] |
| Data at rest | Encryption (AES-256) | [details] |
