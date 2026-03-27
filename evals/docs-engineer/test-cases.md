# Test Cases — docs-engineer

## TC-1: Khởi tạo MkDocs project

- **Prompt:** "Khởi tạo documentation project mới với MkDocs Material"
- **Expected:** mkdocs.yml config, folder structure, markdownlint config
- **Verify:**
  - [ ] Output có `mkdocs.yml` với theme: material
  - [ ] Folder taxonomy theo chuẩn (docs/, operations/, guides/...)
  - [ ] markdownlint config file present

## TC-2: Review markdown quality

- **Prompt:** "Review và fix markdown quality cho thư mục docs/"
- **Expected:** Markdownlint rules, heading hierarchy, code block languages
- **Verify:**
  - [ ] Heading levels tăng dần (MD001)
  - [ ] Code blocks có language specified (MD040)
  - [ ] No trailing spaces (MD009)

## TC-3: Thêm MkDocs components

- **Prompt:** "Thêm admonitions và tabs vào trang documentation"
- **Expected:** Đúng syntax MkDocs-Material admonitions và tabs
- **Verify:**
  - [ ] Admonition syntax: `!!! note/warning/danger`
  - [ ] Tab syntax: `=== "Tab name"`
  - [ ] Render đúng trong MkDocs serve
