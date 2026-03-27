---
title: "ADR-002: Choose PostgreSQL over MongoDB"
description: "Architecture decision — database selection (MADR format)"
author: Demo Team
created: 2026-03-15
updated: 2026-03-15
status: accepted
tags: [adr, database, architecture]
---

# Choose PostgreSQL over MongoDB

!!! info "ADR Metadata"

    | Field               | Value                            |
    | ------------------- | -------------------------------- |
    | **Status**          | Accepted                         |
    | **Date**            | 2026-03-15                       |
    | **Decision-makers** | Tech Lead, DBA, Backend Team     |
    | **Consulted**       | DevOps, Security                 |
    | **Informed**        | All engineering                  |

## Context and Problem Statement

Hệ thống cần persistent database cho user data, transactions, và analytics. Cần chọn giữa SQL và NoSQL approach.

## Decision Drivers

- ACID compliance cho financial transactions
- Team expertise (3/5 developers có PostgreSQL experience)
- Ecosystem maturity và long-term support
- Query flexibility cho reporting

## Considered Options

- PostgreSQL
- MongoDB
- CockroachDB

## Decision Outcome

Chosen option: "PostgreSQL", because nó đáp ứng ACID requirements, team đã có expertise, và ecosystem mature nhất.

### Consequences

!!! success "Good"
    - ACID compliance built-in cho transactions
    - Team không cần training mới

!!! warning "Bad"
    - Horizontal scaling phức tạp hơn MongoDB

!!! note "Neutral"
    - Cả hai đều có managed cloud options

## Pros and Cons of the Options

### PostgreSQL

- Good, because ACID compliant natively
- Good, because team có 3+ years experience
- Good, because excellent JSON support (JSONB) cho flexible schemas
- Bad, because horizontal sharding cần extension (Citus)

### MongoDB

- Good, because horizontal scaling built-in
- Good, because flexible schema cho rapid prototyping
- Bad, because eventual consistency by default
- Bad, because team cần training (2-3 weeks estimated)

### CockroachDB

- Good, because distributed SQL (PostgreSQL compatible)
- Bad, because team không có experience
- Bad, because licensing costs cho enterprise features
