# MkDocs Plugins Catalog — Curated List

> Chọn lọc từ [mkdocs/catalog](https://github.com/mkdocs/catalog) (300+ plugins). Chỉ liệt kê plugins **uy tín, maintained, phù hợp cho documentation project**.

---

## 🎨 Theme (Bắt buộc)

| Plugin                                                          | Stars | Mô tả                                                    | Install                       |
| --------------------------------------------------------------- | ----- | -------------------------------------------------------- | ----------------------------- |
| [mkdocs-material](https://github.com/squidfunk/mkdocs-material) | 22k+  | Theme chính — dark mode, search, navigation, admonitions | `pip install mkdocs-material` |

---

## 🔍 Search & Navigation

| Plugin                                                                             | Mô tả                              | Install                                   |
| ---------------------------------------------------------------------------------- | ---------------------------------- | ----------------------------------------- |
| [mkdocs-awesome-pages](https://github.com/lukasgeiter/mkdocs-awesome-pages-plugin) | Custom nav order via `.pages` file | `pip install mkdocs-awesome-pages-plugin` |
| [mkdocs-literate-nav](https://github.com/oprypin/mkdocs-literate-nav)              | Define nav in Markdown files       | `pip install mkdocs-literate-nav`         |
| [mkdocs-section-index](https://github.com/oprypin/mkdocs-section-index)            | Section index pages                | `pip install mkdocs-section-index`        |

---

## 📊 Charts, Diagrams & Images

| Plugin                                                                 | Mô tả                   | Install                              |
| ---------------------------------------------------------------------- | ----------------------- | ------------------------------------ |
| ~~mkdocs-mermaid2~~ | ~~Mermaid diagrams~~ | **Không cần cho Material >= 9.x** — Mermaid đã built-in qua `pymdownx.superfences` |
| [mkdocs-drawio](https://pypi.org/project/mkdocs-drawio-exporter/)        | Embed draw.io diagrams  | `pip install mkdocs-drawio-exporter` |
| [mkdocs-glightbox](https://pypi.org/project/mkdocs-glightbox/)           | Image lightbox zoom     | `pip install mkdocs-glightbox`       |

---

## 🌲 Git Info & Versioning

| Plugin                                                                                              | Mô tả                       | Install                                                 |
| --------------------------------------------------------------------------------------------------- | --------------------------- | ------------------------------------------------------- |
| [git-revision-date-localized](https://pypi.org/project/mkdocs-git-revision-date-localized-plugin/) | "Last updated" date tự động | `pip install mkdocs-git-revision-date-localized-plugin` |
| [git-authors](https://pypi.org/project/mkdocs-git-authors-plugin/)                                 | Author info từ git history  | `pip install mkdocs-git-authors-plugin`                 |
| [mike](https://pypi.org/project/mike/)                                                             | Multi-version docs          | `pip install mike`                                      |

---

## 🍱 Export & Conversion

| Plugin                                                                      | Mô tả                      | Install                                |
| --------------------------------------------------------------------------- | -------------------------- | -------------------------------------- |
| [mkdocs-print-site](https://pypi.org/project/mkdocs-print-site-plugin/)    | Print-friendly single page | `pip install mkdocs-print-site-plugin` |
| [mkdocs-pdf-export](https://pypi.org/project/mkdocs-pdf-export-plugin/)   | Export pages to PDF        | `pip install mkdocs-pdf-export-plugin` |
| [mkdocs-with-pdf](https://pypi.org/project/mkdocs-with-pdf/)              | Full site PDF generation   | `pip install mkdocs-with-pdf`          |

---

## ✅ Quality & Linting

| Plugin                                                                       | Mô tả                        | Install                                    |
| ---------------------------------------------------------------------------- | ---------------------------- | ------------------------------------------ |
| [markdownlint-cli2](https://github.com/DavidAnson/markdownlint-cli2)        | Markdown lint CLI (CI-ready) | `npm install markdownlint-cli2 --save-dev` |
| [mkdocs-spellcheck](https://pypi.org/project/mkdocs-spellcheck/)            | Spell checking for MkDocs    | `pip install mkdocs-spellcheck`            |
| [mkdocs-htmlproofer](https://pypi.org/project/mkdocs-htmlproofer-plugin/)   | Validate HTML links          | `pip install mkdocs-htmlproofer-plugin`    |

---

## 🌍 i18n & Localization

| Plugin                                                               | Mô tả                       | Install                          |
| -------------------------------------------------------------------- | --------------------------- | -------------------------------- |
| [mkdocs-static-i18n](https://pypi.org/project/mkdocs-static-i18n/) | Multi-language static sites | `pip install mkdocs-static-i18n` |

---

## 📁 Snippets & Includes

| Plugin                                                                               | Mô tả                                 | Install                                      |
| ------------------------------------------------------------------------------------ | ------------------------------------- | -------------------------------------------- |
| [mkdocs-macros](https://pypi.org/project/mkdocs-macros-plugin/)                     | Variables, macros, filters trong docs | `pip install mkdocs-macros-plugin`           |
| [mkdocs-include-markdown](https://pypi.org/project/mkdocs-include-markdown-plugin/) | Include .md files vào pages           | `pip install mkdocs-include-markdown-plugin` |

---

## 🏆 Recommended Stack (Starter)

Cho documentation project tiêu biểu, cài đặt combo sau:

```bash
pip install \
  mkdocs-material \
  mkdocs-awesome-pages-plugin \
  mkdocs-git-revision-date-localized-plugin \
  mkdocs-minify-plugin \
  mkdocs-glightbox \
  mkdocs-print-site-plugin
```

**Tổng: 6 plugins** — đủ cho hầu hết documentation projects.

---

## Sources

- [mkdocs/catalog](https://github.com/mkdocs/catalog) — 300+ MkDocs plugins & projects
- [squidfunk/mkdocs-material](https://squidfunk.github.io/mkdocs-material/) — Official Material theme docs

---

> **Version:** 4.0.0 | **Updated:** 2026-03-30
