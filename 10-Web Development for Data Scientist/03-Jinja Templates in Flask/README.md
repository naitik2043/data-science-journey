# Jinja Templates in Flask

## 📌 What is Jinja2?

Jinja2 is Flask's default templating engine used to create **dynamic HTML pages**.

---

## Folder Structure

```text
03-Jinja Templates in Flask/
│
├── main.py
├── templates/
│   └── index.html
└── README.md
```

---

## Run Project

```bash
pip install flask
python main.py
```

Open:

```
http://127.0.0.1:5000
```

---

# Jinja2 Syntax Cheat Sheet

### Variables

```html
{{ variable }}
```

Example:

```html
{{ name }}
```

---

### For Loop

```html
{% for item in items %}
    {{ item }}
{% endfor %}
```

---

### If-Else

```html
{% if age >= 18 %}
    Adult
{% else %}
    Minor
{% endif %}
```

---

### Comments

```html
{# This is a comment #}
```

---

## Common Filters

```html
{{ name | upper }}
{{ name | lower }}
{{ name | title }}
{{ lucky | length }}
{{ footer | safe }}
{{ city | default("Unknown") }}
```

---

## Passing Data

```python
return render_template(
    "index.html",
    name=name,
    lang=language,
    lucky=luckynos,
    footer=footer
)
```

---

## Quick Revision

| Syntax | Purpose |
|---------|---------|
| `{{ }}` | Display Variable |
| `{% for %}` | Loop |
| `{% if %}` | Condition |
| `{% else %}` | Else Block |
| `{% endif %}` | End If |
| `{% endfor %}` | End Loop |
| `\|upper` | Uppercase |
| `\|lower` | Lowercase |
| `\|title` | Title Case |
| `\|length` | Count Elements |
| `\|safe` | Render HTML |
| `\|default` | Default Value |

---

## Remember

- `{{ }}` → Print values
- `{% %}` → Logic (loops, if-else)
- `{# #}` → Comments
- `render_template()` → Send data from Flask to HTML
- `templates/` → Store HTML files
