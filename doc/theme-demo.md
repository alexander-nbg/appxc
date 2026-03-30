---
orphan: true
---

<!--Copyright 2026 the contributors of APPXC (github.com/alexander-nbg/appxc)-->
<!--SPDX-License-Identifier: 0BSD-->

# Theme Demo

This page is intentionally not linked from the navigation and is used to visually validate common documentation syntax and theme rendering.

## Links

- Internal link via Sphinx role: {doc}`user/scope`
- External link: [PyData Sphinx Theme](https://pydata-sphinx-theme.readthedocs.io/)
- GitHub issue shortcut: [#42](gh)
- GitHub source shortcut: [doc/theme-demo.md](gh)

## Inline Code

Use `Storage` for persistence, and pass `user_id` to `register_user()`.

## Code Blocks

```python
from appxc.config import Stateful

config = Stateful("example")
config["mode"] = "demo"
print(config["mode"])
```

```bash
source .venv/bin/activate
./dev/build_doc.sh --clean
```

## Admonitions

```{note}
This is the info/note color family.
```

```{tip}
This is the success/tip color family.
```

```{warning}
This is the warning color family.
```

```{danger}
This is the danger/error color family.
```

```{caution}
This caution variant should match the warning family.
```

```{error}
This error variant should match the danger family.
```

## Table

| Item | Meaning |
| --- | --- |
| `note` | informational callout |
| `tip` | successful hint |
| `warning` | risk indicator |
| `danger` | strong failure indicator |

## Block Quotes

> This is a simple block quote. It can contain any text or formatting that you would normally use in a paragraph.

> This is a multi-paragraph block quote.
>
> Here is the second paragraph, which provides additional context or elaboration on the first paragraph.
