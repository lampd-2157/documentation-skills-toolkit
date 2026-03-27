# Test Cases — project-doc-writer

## TC-1: Architecture Decision Record

- **Prompt:** "Viết ADR cho quyết định chọn PostgreSQL thay vì MongoDB"
- **Expected:** ADR template đầy đủ
- **Verify:**
  - [ ] Header: Status, Date, Author, Reviewers
  - [ ] Context section giải thích vấn đề
  - [ ] Alternatives Considered table với pros/cons
  - [ ] Consequences: Positive, Negative, Risks

## TC-2: Technical spec

- **Prompt:** "Viết technical spec cho tính năng authentication mới"
- **Expected:** Tech spec template đầy đủ
- **Verify:**
  - [ ] Overview: Goal, Scope
  - [ ] Design: Architecture Diagram (Mermaid), Data Flow
  - [ ] API Contracts table (nếu có)
  - [ ] Implementation Plan với phases + ETA
  - [ ] Testing Strategy table
  - [ ] Rollout Plan

## TC-3: How-to guide

- **Prompt:** "Tạo how-to guide setup Google Workspace cho user mới"
- **Expected:** Guide theo Google Style 4-part structure
- **Verify:**
  - [ ] Prerequisites checklist
  - [ ] Steps với commands + expected result
  - [ ] Verify section
  - [ ] Troubleshooting với common errors

## TC-4: Quick reference card

- **Prompt:** "Làm cheat sheet cho Docker commands thường dùng"
- **Expected:** Quick reference template
- **Verify:**
  - [ ] Essential Commands table (Action, Command, Example)
  - [ ] Common Patterns code blocks
  - [ ] Glossary table
  - [ ] Không quá 2 trang khi in
