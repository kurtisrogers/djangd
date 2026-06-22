"""Storybook variant declarations.

Each entry is ``"story-id": ("<component-name>", {props, optionally __children__})``.
Render them via ``storybook/scripts/render.py`` — every Storybook story
loads its HTML from ``public/rendered/<story-id>.html`` so the Django
templates remain the single source of truth.

For compositions that need free-form HTML (multi-component layouts, demo
chrome around a component), use the special component name ``"__html__"``
and pass a literal string as the second tuple element.
"""
from __future__ import annotations

# ---------------------------------------------------------------------------
# Inputs
# ---------------------------------------------------------------------------

_BUTTON_BASE = {"label": "Save changes", "size": "medium"}

VARIANTS: dict[str, tuple] = {
    "button__raised":     ("button", {**_BUTTON_BASE, "variant": "raised"}),
    "button__outlined":   ("button", {**_BUTTON_BASE, "variant": "outlined"}),
    "button__text":       ("button", {**_BUTTON_BASE, "variant": "text", "label": "Cancel"}),
    "button__unelevated": ("button", {**_BUTTON_BASE, "variant": "unelevated"}),
    "button__with_icon":  ("button", {**_BUTTON_BASE, "variant": "raised", "icon": "save"}),
    "button__link":       ("button", {**_BUTTON_BASE, "variant": "outlined", "href": "#", "label": "Read docs"}),
    "button__disabled":   ("button", {**_BUTTON_BASE, "variant": "raised", "disabled": True}),
    "button__small":      ("button", {**_BUTTON_BASE, "variant": "raised", "size": "small"}),
    "button__large":      ("button", {**_BUTTON_BASE, "variant": "raised", "size": "large"}),

    # Icon buttons
    "icon_button__default": ("icon_button", {"icon": "favorite", "label": "Like"}),
    "icon_button__toggled": ("icon_button", {"icon": "bookmark", "label": "Saved", "toggled": True}),

    # Floating action button
    "fab__default":  ("fab", {"icon": "add", "label": "Create"}),
    "fab__extended": ("fab", {"icon": "edit", "label": "Compose", "extended": True}),

    # Chip
    "chip__default":   ("chip", {"label": "Filter"}),
    "chip__selected":  ("chip", {"label": "Selected", "selected": True}),
    "chip__removable": ("chip", {"label": "Tag", "removable": True, "trailing_icon": "close"}),

    # Text field
    "text_field__filled":   ("text_field", {"label": "Email", "name": "email", "variant": "filled",   "helper": "We never share your address."}),
    "text_field__outlined": ("text_field", {"label": "Email", "name": "email", "variant": "outlined", "helper": "We never share your address."}),
    "text_field__error":    ("text_field", {"label": "Email", "name": "email", "variant": "filled",   "helper": "Please enter a valid email", "error": True, "value": "not-an-email"}),
    "text_field__textarea": ("text_field", {"label": "Notes", "name": "notes", "variant": "outlined", "rows": 4}),

    # Selection
    "checkbox__default":     ("checkbox", {"label": "I agree to the terms", "name": "agree", "checked": True}),
    "radio__default":        ("radio",    {"label": "Option A", "name": "opt", "value": "a", "checked": True}),
    "switch__default":       ("switch",   {"label": "Enable notifications", "name": "notif", "checked": True}),
    "form_field__default":   ("form_field",   {"label": "Subscribe", "__children__": '<div class="mdc-switch djangd-switch mdc-switch--selected"></div>'}),

    "select__filled": ("select", {
        "label": "Country", "name": "country", "variant": "filled",
        "options": ({"value": "uk", "label": "United Kingdom"},
                    {"value": "us", "label": "United States"},
                    {"value": "ie", "label": "Ireland"}),
        "value": "uk",
    }),
    "slider__default": ("slider", {"label": "Volume", "name": "vol", "value": 35, "discrete": True}),

    # Autocomplete
    "autocomplete__default": ("autocomplete", {
        "label": "City", "name": "city", "placeholder": "Start typing…",
        "helper": "Suggestions appear as you type",
        "options": ("Aurora", "Borealis", "Cascade", "Drift", "Eclipse", "Fjord"),
    }),
    "autocomplete__disabled": ("autocomplete", {
        "label": "City", "name": "city", "disabled": True,
        "options": ("Aurora", "Borealis", "Cascade"),
    }),

    # Button group — pre-rendered child buttons go through the registry too.
    "button_group__horizontal": ("__html__", None),  # filled in below
    "button_group__vertical":   ("__html__", None),
    "button_group__contained":  ("__html__", None),

    # Transfer list
    "transfer_list__default": ("transfer_list", {
        "label": "Roles",
        "source_title": "Available",
        "target_title": "Selected",
        "source_items": ("Alpha", "Bravo", "Charlie", "Delta", "Echo"),
        "target_items": ("Foxtrot", "Golf"),
    }),

    # Modern inputs
    "input_otp__default": ("input_otp", {"label": "Verification code", "name": "otp", "helper": "Enter the 6-digit code we just sent you."}),
    "input_otp__masked":  ("input_otp", {"label": "PIN", "name": "pin", "mask": True}),
    "file_upload__default":  ("file_upload",  {"name": "doc", "hint": "PNG, JPG up to 5 MB"}),
    "file_upload__multiple": ("file_upload",  {"name": "docs", "hint": "Drop multiple files", "multiple": True}),
    "toggle__on":  ("toggle", {"text": "Bold", "icon": "format_bold", "pressed": True}),
    "toggle__off": ("toggle", {"text": "Bold", "icon": "format_bold", "pressed": False}),
    "toggle__outline": ("toggle", {"text": "Italic", "icon": "format_italic", "variant": "outline"}),
    "date_picker__default": ("date_picker", {"label": "Departure date", "name": "depart", "value": "2026-09-01"}),

    # ---------------------------------------------------------------------------
    # Surfaces
    # ---------------------------------------------------------------------------
    "card__elevated": ("__html__", None),
    "card__outlined": ("__html__", None),
    "paper__default": ("paper", {"elevation": 2, "__children__":
        '<div style="padding:16px;">Paper surface (elevation 2)</div>'}),
    "divider__default": ("divider", {}),

    # ---------------------------------------------------------------------------
    # Navigation
    # ---------------------------------------------------------------------------
    "app_bar__default": ("app_bar", {"title": "djangd"}),
    "breadcrumbs__default": ("breadcrumbs", {
        "items": ({"label": "Home",     "href": "#"},
                  {"label": "Inbox",    "href": "#"},
                  {"label": "Threads",  "href": None}),
    }),
    "pagination__default": ("pagination", {"page": 3, "total": 8, "url": "?page="}),
    "menu__default": ("menu", {
        "open": True,
        "items": ({"label": "Profile",  "icon": "person"},
                  {"label": "Settings", "icon": "settings"},
                  {"label": "Sign out", "icon": "logout"}),
    }),
    "tab_bar__default": ("tab_bar", {
        "tabs": ({"label": "Inbox", "icon": "inbox"},
                 {"label": "Sent",  "icon": "send"},
                 {"label": "Drafts","icon": "drafts"}),
        "active": 0,
    }),
    "link__body":    ("link", {"text": "Read the docs", "href": "#"}),
    "link__button":  ("link", {"text": "Continue →",    "href": "#", "variant": "button", "underline": "none"}),
    "link__inherit": ("link", {"text": "Inline link",   "href": "#", "color": "inherit"}),

    # ---------------------------------------------------------------------------
    # Data display
    # ---------------------------------------------------------------------------
    "list__two_line": ("list", {
        "two_line": True,
        "items": ({"label": "Kurtis Rogers", "secondary": "kurtis@example.com"},
                  {"label": "Jane Doe",      "secondary": "jane@example.com"},
                  {"label": "Alex Bauer",    "secondary": "alex@example.com"}),
    }),
    "table__default": ("table", {
        "columns": ("Name", "Email", "Role"),
        "rows": (("Kurtis Rogers", "kurtis@example.com", "Owner"),
                 ("Jane Doe",      "jane@example.com",   "Editor"),
                 ("Alex Bauer",    "alex@example.com",   "Viewer")),
        "sticky_header": True,
    }),
    "avatar__default":  ("avatar", {"initials": "KR", "alt": "Kurtis Rogers", "size": "medium"}),
    "avatar__image":    ("avatar", {"src": "https://i.pravatar.cc/96?img=12", "alt": "Avatar", "size": "large"}),
    "badge__default":   ("badge",  {"value": 3}),
    "tooltip__default": ("tooltip", {"text": "Open settings"}),
    "typography__sample": ("__html__", None),

    "timeline__default": ("timeline", {
        "items": (
            {"title": "Order placed",        "time": "Today 10:42", "description": "We've received your order.",    "icon": "shopping_cart", "active": True},
            {"title": "Payment confirmed",   "time": "Today 10:43", "description": "Your card has been charged.",   "icon": "credit_card",   "active": True},
            {"title": "Shipped",             "time": "Tomorrow",    "description": "Royal Mail tracked 24h.",       "icon": "local_shipping","active": False},
            {"title": "Delivered",           "time": "Friday",      "description": "Signature required at door.",  "icon": "check_circle",  "active": False},
        ),
    }),
    "tree_view__default": ("tree_view", {
        "nodes": (
            {"label": "src", "icon": "folder", "expanded": True, "children": (
                {"label": "components", "icon": "folder", "expanded": True, "children": (
                    {"label": "Button.tsx", "icon": "description"},
                    {"label": "Card.tsx",   "icon": "description", "selected": True},
                )},
                {"label": "utils", "icon": "folder", "children": (
                    {"label": "format.ts", "icon": "description"},
                )},
                {"label": "index.ts", "icon": "description"},
            )},
        ),
    }),
    "stat__up":   ("stat", {"label": "Monthly revenue", "value": "£28,420", "delta": "+12%", "delta_label": "vs last month", "trend": "up",   "icon": "paid"}),
    "stat__down": ("stat", {"label": "Refunds",         "value": "£820",    "delta": "-3%",  "delta_label": "vs last month", "trend": "down", "icon": "undo"}),

    "avatar_group__default": ("avatar_group", {
        "avatars": ({"initials": "KR", "alt": "Kurtis"},
                    {"initials": "JD", "alt": "Jane"},
                    {"initials": "AB", "alt": "Alex"},
                    {"initials": "SR", "alt": "Sam"},
                    {"initials": "MK", "alt": "Mei"},
                    {"initials": "TL", "alt": "Tom"},
                    {"initials": "RP", "alt": "Riya"}),
        "max": 4,
    }),

    "kbd__cmd_k":    ("kbd", {"keys": ("⌘", "K")}),
    "kbd__ctrl_s":   ("kbd", {"keys": ("Ctrl", "S"), "size": "sm"}),
    "kbd__cmd_enter": ("kbd", {"keys": ("⌘", "Enter"), "size": "lg"}),

    "status__online":  ("status", {"text": "Online",          "tone": "online"}),
    "status__away":    ("status", {"text": "Away",            "tone": "away", "pulse": True}),
    "status__busy":    ("status", {"text": "Do not disturb",  "tone": "busy"}),
    "status__offline": ("status", {"text": "Offline",         "tone": "offline"}),

    "calendar__default": ("__html__", None),  # built below from the registry

    # ---------------------------------------------------------------------------
    # Feedback
    # ---------------------------------------------------------------------------
    "alert__info":    ("alert", {"severity": "info",    "title": "Heads up",    "message": "Your invoice will be issued on the 1st."}),
    "alert__success": ("alert", {"severity": "success", "title": "All saved",   "message": "Your changes are now live."}),
    "alert__warning": ("alert", {"severity": "warning", "title": "Heads up",    "message": "Your trial ends in 3 days."}),
    "alert__error":   ("alert", {"severity": "error",   "title": "Couldn't save","message": "Try again, or contact support."}),
    "snackbar__default": ("snackbar", {"message": "Message sent", "action_label": "Undo"}),
    "linear_progress__indeterminate": ("linear_progress", {"indeterminate": True}),
    "circular_progress__indeterminate": ("circular_progress", {"indeterminate": True}),
    "skeleton__rectangular": ("skeleton", {"variant": "rectangular", "height": "120px"}),

    # Overlays
    "backdrop__open":   ("__html__", None),
    "modal__open":      ("__html__", None),
    "popover__bottom":  ("__html__", None),
    "hover_card__default": ("__html__", None),
    "sheet__right":     ("__html__", None),
    "command__open":    ("__html__", None),
    "empty_state__default": ("empty_state", {
        "title": "No invoices yet",
        "description": "Create your first invoice to start tracking payments.",
        "icon": "receipt_long",
        "actions": (
            '<button class="mdc-button mdc-button--outlined djangd-button" type="button"><span class="mdc-button__label">Import</span></button>',
            '<button class="mdc-button mdc-button--raised djangd-button djangd-button--raised" type="button"><span class="mdc-button__label">Create invoice</span></button>',
        ),
    }),

    # ---------------------------------------------------------------------------
    # Layout / utility
    # ---------------------------------------------------------------------------
    "container__lg":  ("container", {"max_width": "lg", "padded": True, "__children__":
        '<p style="margin:0;">Centred max-width container with padding.</p>'}),
    "grid__12":       ("__html__", None),
    "stack__row":     ("__html__", None),
    "box__surface":   ("box",  {"padding": "4", "surface": "variant", "rounded": "md", "__children__":
        "Box content — composes padding / surface / rounded modifiers via class names."}),
    "box__flex_row":  ("box",  {"display": "flex", "align": "center", "justify": "between", "padding": "4", "surface": "variant", "rounded": "md", "__children__":
        '<strong>Left</strong><span>Middle</span><em>Right</em>'}),

    "aspect_ratio__16_9": ("aspect_ratio", {"ratio": "16 / 9", "__children__":
        '<div style="background:var(--djangd-color-surface-variant);display:flex;align-items:center;justify-content:center;color:var(--djangd-color-on-surface-variant);">16 / 9</div>'}),
    "scroll_area__default": ("scroll_area", {"max_height": "200px", "max_width": "360px", "__children__":
        "".join(f"<p style='margin:8px 0;'>Item {i+1} — a long row in a scrollable container.</p>" for i in range(25))}),
    "toolbar__editor": ("toolbar", {
        "items": (
            '<button class="djangd-icon-button mdc-icon-button" aria-label="Bold"><i class="material-icons">format_bold</i></button>',
            '<button class="djangd-icon-button mdc-icon-button" aria-label="Italic"><i class="material-icons">format_italic</i></button>',
            '<button class="djangd-icon-button mdc-icon-button" aria-label="Underline"><i class="material-icons">format_underlined</i></button>',
            '<span class="djangd-divider djangd-divider--vertical" style="width:1px;height:24px;background:var(--djangd-color-outline);"></span>',
            '<button class="djangd-icon-button mdc-icon-button" aria-label="Bulleted list"><i class="material-icons">format_list_bulleted</i></button>',
            '<button class="djangd-icon-button mdc-icon-button" aria-label="Numbered list"><i class="material-icons">format_list_numbered</i></button>',
        ),
        "elevated": True,
    }),
    "carousel__default": ("carousel", {
        "slides": (
            {"html": '<div style="height:280px;background:#6750a4;color:#fff;display:flex;align-items:end;justify-content:flex-start;padding:24px;"><div class="djangd-carousel__caption">Aurora</div></div>'},
            {"html": '<div style="height:280px;background:#7d5260;color:#fff;display:flex;align-items:end;justify-content:flex-start;padding:24px;"><div class="djangd-carousel__caption">Solstice</div></div>'},
            {"html": '<div style="height:280px;background:#2e7d32;color:#fff;display:flex;align-items:end;justify-content:flex-start;padding:24px;"><div class="djangd-carousel__caption">Borealis</div></div>'},
        ),
        "active": 0,
    }),
    "visually_hidden__example": ("__html__",
        '<button class="mdc-button mdc-button--outlined djangd-button" type="button">'
        '<i class="material-icons" aria-hidden="true">delete</i>'
        '<span class="djangd-visually-hidden">Delete item</span>'
        "</button>"
    ),
}


# ---------------------------------------------------------------------------
# Compositions that need the registry to render child components first.
# ---------------------------------------------------------------------------

def _populate_compositions() -> None:
    """Fill in ``__html__`` placeholder variants by composing rendered children."""
    import django
    from django.conf import settings as _settings

    if not _settings.configured:
        _settings.configure(
            DEBUG=False,
            INSTALLED_APPS=["django.contrib.contenttypes", "django.contrib.auth", "djangd_framework"],
            DATABASES={"default": {"ENGINE": "django.db.backends.sqlite3", "NAME": ":memory:"}},
            TEMPLATES=[{
                "BACKEND": "django.template.backends.django.DjangoTemplates",
                "APP_DIRS": True,
                "OPTIONS": {"context_processors": []},
            }],
            USE_TZ=True,
            DEFAULT_AUTO_FIELD="django.db.models.BigAutoField",
        )
        django.setup()
    import djangd_framework.components  # noqa: F401
    from djangd_framework.registry import registry

    def render(name: str, props: dict, children: str = "") -> str:
        cls = registry.get(name)
        return cls(props=dict(props), children=children).render()

    # ---- Button group ------------------------------------------------------
    btn_outlined = lambda label: render("button", {"label": label, "variant": "outlined"})  # noqa: E731
    btn_raised   = lambda label: render("button", {"label": label, "variant": "raised"})    # noqa: E731

    VARIANTS["button_group__horizontal"] = ("button_group", {
        "label": "Text alignment", "orientation": "horizontal", "variant": "outlined",
        "buttons": (btn_outlined("Left"), btn_outlined("Centre"), btn_outlined("Right")),
    })
    VARIANTS["button_group__vertical"] = ("button_group", {
        "label": "Text alignment", "orientation": "vertical", "variant": "outlined",
        "buttons": (btn_outlined("Left"), btn_outlined("Centre"), btn_outlined("Right")),
    })
    VARIANTS["button_group__contained"] = ("button_group", {
        "label": "Text alignment", "orientation": "horizontal", "variant": "contained",
        "buttons": (btn_raised("Left"), btn_raised("Centre"), btn_raised("Right")),
    })

    # ---- Card --------------------------------------------------------------
    card_inner = (
        '<div class="mdc-card__media" style="background-image:url(\'https://placehold.co/720x405/eaddff/21005d.png?text=djangd\');background-size:cover;height:160px;" role="img" aria-label="Hero image"></div>'
        '<div class="mdc-card__content" style="padding:16px;">'
        '<h2 class="djangd-typography djangd-typography--title-large" style="margin:0 0 8px;">Material card</h2>'
        '<p class="djangd-typography djangd-typography--body-medium" style="margin:0;color:var(--djangd-color-on-surface-variant);">Cards contain content and actions about a single subject.</p>'
        "</div>"
        '<div class="mdc-card__actions" style="display:flex;gap:8px;padding:8px 16px 16px;">'
        + render("button", {"label": "Cancel", "variant": "text"})
        + render("button", {"label": "Confirm", "variant": "raised"})
        + "</div>"
    )
    VARIANTS["card__elevated"] = ("card", {"__children__": card_inner})
    VARIANTS["card__outlined"] = ("card", {"outlined": True, "__children__": card_inner})

    # ---- Calendar ----------------------------------------------------------
    weeks = (
        ({"day": 27, "outside": True},  {"day": 28, "outside": True},
         {"day": 29, "outside": True},  {"day": 30, "outside": True},
         {"day": 31, "outside": True},  {"day": 1,  "iso": "2026-08-01"},
         {"day": 2,  "iso": "2026-08-02"}),
        tuple({"day": d, "iso": f"2026-08-{d:02d}"} for d in range(3, 10)),
        tuple({"day": d, "iso": f"2026-08-{d:02d}",
               "today": d == 15} for d in range(10, 17)),
        tuple({"day": d, "iso": f"2026-08-{d:02d}",
               "selected": d == 21} for d in range(17, 24)),
        tuple({"day": d, "iso": f"2026-08-{d:02d}"} for d in range(24, 31)),
        ({"day": 31, "iso": "2026-08-31"},
         {"day": 1,  "outside": True}, {"day": 2,  "outside": True},
         {"day": 3,  "outside": True}, {"day": 4,  "outside": True},
         {"day": 5,  "outside": True}, {"day": 6,  "outside": True}),
    )
    VARIANTS["calendar__default"] = ("calendar", {
        "month": "August", "year": 2026, "weeks": weeks,
    })

    # ---- Overlays demos: wrap the real component in a demo backdrop -------
    backdrop_demo = (
        '<div style="position:relative;height:240px;border:1px dashed var(--djangd-color-outline);overflow:hidden;">'
        '<p style="padding:16px;">Page content under the backdrop.</p>'
        + render("backdrop", {"open": True}, children=(
            render("paper", {"elevation": 3}, children='<div style="padding:16px;">Loading…</div>')
        ))
        + "</div>"
    )
    VARIANTS["backdrop__open"] = ("__html__", backdrop_demo)

    modal_inner = (
        '<h2 id="modal-title" style="margin:0 0 8px 0;">Confirm action</h2>'
        '<p style="margin:0 0 16px 0;">Are you sure you want to continue?</p>'
        '<div style="display:flex;gap:8px;justify-content:flex-end;">'
        + render("button", {"label": "Cancel", "variant": "outlined"})
        + render("button", {"label": "Confirm", "variant": "raised"})
        + "</div>"
    )
    modal_demo = (
        '<div style="position:relative;height:320px;border:1px dashed var(--djangd-color-outline);overflow:hidden;">'
        '<p style="padding:16px;">Page content under the modal.</p>'
        '<div aria-hidden="true" style="position:absolute;inset:0;background:rgba(0,0,0,.5);"></div>'
        + render("modal", {"open": True, "labelledby": "modal-title"}, children=modal_inner).replace(
            'class="djangd-modal ',
            'style="position:absolute;top:50%;left:50%;transform:translate(-50%,-50%);" class="djangd-modal ')
        + "</div>"
    )
    VARIANTS["modal__open"] = ("__html__", modal_demo)

    popover_demo = (
        '<div style="position:relative;height:180px;padding:60px;">'
        + render("button", {"label": "Trigger", "variant": "raised"})
        + render("popover", {"open": True, "placement": "bottom"}, children="Quick info goes here.")
        .replace('class="djangd-popover ', 'style="top:70px;left:60px;" class="djangd-popover ')
        + "</div>"
    )
    VARIANTS["popover__bottom"] = ("__html__", popover_demo)

    hover_card_demo = (
        '<p style="font-family:var(--djangd-font-family);max-width:60ch;">'
        "Click the "
        + render("hover_card", {
            "trigger": "@kurtisrogers", "placement": "bottom",
        }, children=(
            "<strong>Kurtis Rogers</strong><br/>"
            "Building djangd-framework.<br/>"
            '<small style="color:var(--djangd-color-on-surface-variant);">Joined Jun 2026 — UK</small>'
        ))
        + " handle to see a quick profile card."
        + "</p>"
    )
    VARIANTS["hover_card__default"] = ("__html__", hover_card_demo)

    sheet_actions = (
        render("button", {"label": "Reset",  "variant": "outlined"}),
        render("button", {"label": "Apply",  "variant": "raised"}),
    )
    sheet_demo = (
        '<div style="position:relative;height:360px;border:1px dashed var(--djangd-color-outline);overflow:hidden;">'
        '<p style="padding:16px;">Page content beneath the sheet.</p>'
        + render("sheet", {
            "open": True, "side": "right", "title": "Filters",
            "actions": sheet_actions,
        }, children="<p>Configure your view from here. This panel scrolls when content overflows.</p>")
        + "</div>"
    )
    VARIANTS["sheet__right"] = ("__html__", sheet_demo)

    command_demo = (
        '<div style="position:relative;height:420px;border:1px dashed var(--djangd-color-outline);overflow:hidden;background:var(--djangd-color-background);">'
        '<p style="padding:16px;">Press '
        + render("kbd", {"keys": ("⌘", "K")})
        + " to open.</p>"
        + render("command", {
            "open": True,
            "groups": (
                {"heading": "Navigation", "commands": (
                    {"label": "Go to dashboard", "icon": "home",   "shortcut": "G D"},
                    {"label": "Open profile",   "icon": "person", "shortcut": "G P"},
                )},
                {"heading": "Actions",    "commands": (
                    {"label": "Create new project", "icon": "add",   "shortcut": "N P"},
                    {"label": "Share workspace",    "icon": "share"},
                )},
            ),
        })
        + "</div>"
    )
    VARIANTS["command__open"] = ("__html__", command_demo)

    # ---- Layout compositions ----------------------------------------------
    grid_cells = "".join(
        '<div class="djangd-grid__cell"><div class="djangd-paper djangd-paper--elevation-1" style="text-align:center;padding:12px;">'
        f"{i + 1}</div></div>"
        for i in range(12)
    )
    VARIANTS["grid__12"] = ("__html__",
        f'<div class="djangd-grid djangd-grid--cols-12 djangd-grid--gap-md">{grid_cells}</div>')

    stack_inner = (
        render("button", {"label": "Cancel", "variant": "outlined"})
        + render("button", {"label": "Save",   "variant": "raised"})
    )
    VARIANTS["stack__row"] = ("__html__",
        '<div class="djangd-stack djangd-stack--horizontal djangd-stack--gap-md djangd-stack--align-center">'
        + stack_inner + "</div>")

    # ---- Typography sample -------------------------------------------------
    VARIANTS["typography__sample"] = ("__html__",
        "".join(
            f'<p class="djangd-typography djangd-typography--{variant}">{variant.replace("-", " ")}</p>'
            for variant in (
                "display-medium", "headline-large", "title-large",
                "body-large", "body-medium", "label-large",
            )
        ))


_populate_compositions()
