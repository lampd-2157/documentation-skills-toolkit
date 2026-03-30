---
title: "Architecture — E-Commerce Platform"
status: approved
updated: 2026-03-30
tags:
  - architecture
  - T12
  - example
---

# E-Commerce Platform — Architecture

!!! info "Document Metadata"
    | Field | Value |
    |-------|-------|
    | **Owner** | Platform Team |
    | **Status** | Approved |
    | **Last reviewed** | 2026-03-30 |
    | **Scope** | Full platform architecture — order flow focus |

## Context Diagram

High-level view: how the platform interacts with users and external systems.

```mermaid
graph TB
    CUST[Customers] -->|HTTPS| WEB[E-Commerce Platform]
    ADMIN[Admin Staff] -->|HTTPS| WEB
    WEB -->|REST API| PAY[Payment Gateway<br/>Stripe]
    WEB -->|SMTP| EMAIL[Email Service<br/>SendGrid]
    WEB -->|API| SHIP[Shipping Provider<br/>GHN API]
    WEB -->|Webhook| ANALYTICS[Analytics<br/>Mixpanel]
```

| Actor / System | Interaction | Protocol | Notes |
|----------------|-------------|----------|-------|
| Customers | Browse, order, payment | HTTPS | Web + Mobile responsive |
| Admin Staff | Manage products, orders | HTTPS | Internal admin panel |
| Stripe | Payment processing | REST API | PCI-DSS compliant |
| SendGrid | Transactional emails | SMTP/API | Order confirmation, shipping updates |
| GHN API | Shipping tracking | REST API | Vietnam domestic shipping |

## Component Diagram

Internal components and how they communicate.

```mermaid
graph LR
    subgraph Frontend
        WEB[Web App<br/>Next.js]
        ADMIN_UI[Admin Panel<br/>React]
    end
    subgraph Backend
        GW[API Gateway<br/>Kong]
        ORDER[Order Service]
        PRODUCT[Product Service]
        USER[User Service]
        NOTIFY[Notification Worker]
    end
    subgraph Data
        PG[(PostgreSQL)]
        REDIS[(Redis Cache)]
        RABBIT[RabbitMQ]
        S3[S3 — Images]
    end

    WEB & ADMIN_UI --> GW
    GW --> ORDER & PRODUCT & USER
    ORDER & PRODUCT & USER --> PG
    ORDER & PRODUCT --> REDIS
    ORDER --> RABBIT --> NOTIFY
    PRODUCT --> S3
```

| Component | Responsibility | Technology | Owner |
|-----------|---------------|------------|-------|
| API Gateway | Routing, rate limiting, auth | Kong 3.x | Platform Team |
| Order Service | Order lifecycle, checkout | Node.js (Express) | Order Team |
| Product Service | Catalog, inventory, search | Node.js (Express) | Product Team |
| User Service | Auth, profiles, addresses | Node.js (Express) | Platform Team |
| Notification Worker | Email, SMS, push notifications | Node.js | Platform Team |
| PostgreSQL | Persistent storage | PostgreSQL 16 | DBA Team |
| Redis | Cache, session, rate limiting | Redis 7.2 | Platform Team |

## Data Flow

How data moves through the system for the checkout flow.

```mermaid
sequenceDiagram
    participant C as Customer
    participant GW as API Gateway
    participant O as Order Service
    participant P as Product Service
    participant DB as PostgreSQL
    participant PAY as Stripe
    participant Q as RabbitMQ
    participant N as Notification Worker

    C->>GW: POST /orders (cart items)
    GW->>O: Create order
    O->>P: Check inventory
    P->>DB: SELECT stock
    DB-->>P: Stock available
    P-->>O: Inventory confirmed
    O->>DB: INSERT order (status: pending)
    O->>PAY: Create payment intent
    PAY-->>O: Payment confirmed
    O->>DB: UPDATE order (status: paid)
    O->>Q: order.paid event
    Q->>N: Process notification
    N->>N: Send confirmation email
    O-->>GW: Order response
    GW-->>C: 201 Created
```

| Flow | Trigger | Path | SLA |
|------|---------|------|-----|
| Checkout | Customer places order | Customer -> Gateway -> Order -> Product -> DB -> Stripe | < 3s end-to-end |
| Order notification | Payment confirmed | Order -> Queue -> Worker -> SendGrid | < 30s after payment |
| Inventory sync | Product update | Admin -> Product -> DB -> Cache invalidation | < 1s cache refresh |

## Technology Stack

| Layer | Technology | Version | Purpose |
|-------|-----------|---------|---------|
| Frontend | Next.js | 14.x | SSR + static pages for SEO |
| Admin UI | React + Ant Design | 18.x | Internal management dashboard |
| Backend | Node.js + Express | 20 LTS | API services |
| Database | PostgreSQL | 16 | Primary data store |
| Cache | Redis | 7.2 | Session, product cache, rate limiting |
| Queue | RabbitMQ | 3.13 | Async event processing |
| Storage | MinIO (S3-compatible) | latest | Product images |
| Infrastructure | Docker + K8s | 1.29 | Container orchestration |

## Deployment View

```mermaid
graph TB
    subgraph Production
        LB[Nginx Load Balancer]
        subgraph Node-1
            APP1[App Pod x3]
            WORKER1[Worker Pod x2]
        end
        subgraph Node-2
            APP2[App Pod x3]
            WORKER2[Worker Pod x2]
        end
        subgraph Data-Node
            PG1[(PostgreSQL Primary)]
            PG2[(PostgreSQL Replica)]
            REDIS1[(Redis Primary)]
        end
    end
    LB --> APP1 & APP2
    PG1 -.->|streaming replication| PG2
```

| Environment | Instances | Region | Notes |
|-------------|-----------|--------|-------|
| Production | 3 nodes K8s | `<REGION>` | Auto-scaling 3-6 app pods |
| Staging | 1 node K8s | `<REGION>` | Mirrors prod config |
| Development | Docker Compose | Local | Single-node all services |

## Security Boundaries

```mermaid
graph TB
    subgraph Public Zone
        CDN[CDN — CloudFlare]
        LB[Load Balancer]
    end
    subgraph DMZ
        WAF[WAF Rules]
        GW[API Gateway — Kong]
    end
    subgraph Private Zone
        SVC[Application Services]
        DB[(Database)]
        QUEUE[Message Queue]
    end
    CDN --> LB --> WAF --> GW --> SVC --> DB
    SVC --> QUEUE
```

| Boundary | Controls | Notes |
|----------|----------|-------|
| Public -> DMZ | CloudFlare WAF, DDoS protection, TLS 1.3 | Rate limit: 100 req/min per IP |
| DMZ -> Private | Kong auth, JWT validation, network ACL | Service mesh with mTLS |
| Data at rest | AES-256 encryption | PostgreSQL TDE + S3 SSE |
| Secrets | HashiCorp Vault | Auto-rotation every 90 days |
