"""Built-in Material components, registered on app ready.

Every component is a thin subclass of :class:`djangd_framework.Component`
that points at a BEM-styled template under ``templates/djangd/components/``.

The registrations here form the **single source of truth** for the
component library — adding a new built-in component just means creating a
template, a class here, and a story under ``storybook/stories/``.

To extend or override any component in user code::

    from djangd_framework import Component, register

    @register(replace=True)
    class Button(Component):
        name = "button"
        template = "myapp/button.html"  # your own template

Or to add a brand-new component::

    @register
    class Alert(Component):
        name = "myapp.alert"
        template = "myapp/alert.html"
        defaults = {"severity": "info"}
        required_props = ("message",)
"""
from __future__ import annotations

from typing import ClassVar

from ..registry import Component, register, registry

# A compact metaclass-free way to declare lots of similar components.


def _make(
    name: str,
    template: str,
    defaults: dict | None = None,
    allowed: tuple[str, ...] | None = None,
    required: tuple[str, ...] = (),
    group: str = "misc",
    scss: tuple[str, ...] = (),
) -> type[Component]:
    cls = type(
        f"{name.replace('.', '_').title()}Component",
        (Component,),
        {
            "name": name,
            "template": template,
            "defaults": dict(defaults or {}),
            "allowed_props": allowed,
            "required_props": required,
            "group": group,
            "scss_partials": tuple(scss),
        },
    )
    return register(cls, source="builtin")


# ---------------------------------------------------------------------------
# Inputs & actions
# ---------------------------------------------------------------------------
_make(
    "button",
    "djangd/components/button.html",
    defaults={
        "label": "",
        "variant": "text",  # text | outlined | raised | unelevated
        "type": "button",
        "disabled": False,
        "icon": None,
        "trailing_icon": False,
        "href": None,
        "size": "medium",  # small | medium | large
    },
    required=("label",),
)
_make(
    "icon_button",
    "djangd/components/icon_button.html",
    defaults={"icon": "favorite", "label": "", "toggled": False, "disabled": False},
    required=("icon", "label"),
)
_make(
    "fab",
    "djangd/components/fab.html",
    defaults={"icon": "add", "label": "", "extended": False, "mini": False, "exited": False},
    required=("icon", "label"),
)
_make(
    "chip",
    "djangd/components/chip.html",
    defaults={"label": "", "icon": None, "trailing_icon": None, "selected": False, "removable": False},
    required=("label",),
)
_make(
    "text_field",
    "djangd/components/text_field.html",
    defaults={
        "variant": "filled",  # filled | outlined
        "label": "",
        "name": "",
        "value": "",
        "type": "text",
        "placeholder": "",
        "helper": "",
        "error": False,
        "required": False,
        "disabled": False,
        "leading_icon": None,
        "trailing_icon": None,
        "id": None,
        "rows": None,  # if set, renders <textarea>
    },
    required=("label",),
)
_make(
    "checkbox",
    "djangd/components/checkbox.html",
    defaults={"label": "", "name": "", "value": "1", "checked": False, "disabled": False, "indeterminate": False, "id": None},
)
_make(
    "radio",
    "djangd/components/radio.html",
    defaults={"label": "", "name": "", "value": "", "checked": False, "disabled": False, "id": None},
    required=("name", "value"),
)
_make(
    "switch",
    "djangd/components/switch.html",
    defaults={"label": "", "name": "", "checked": False, "disabled": False, "id": None},
)
_make(
    "select",
    "djangd/components/select.html",
    defaults={"label": "", "name": "", "options": (), "value": "", "variant": "filled", "helper": "", "required": False, "disabled": False, "id": None},
    required=("label", "options"),
)
_make(
    "slider",
    "djangd/components/slider.html",
    defaults={"label": "", "name": "", "min": 0, "max": 100, "step": 1, "value": 50, "discrete": False, "disabled": False, "id": None},
)
_make(
    "form_field",
    "djangd/components/form_field.html",
    defaults={"label": "", "align_end": False},
)

# ---------------------------------------------------------------------------
# Surfaces
# ---------------------------------------------------------------------------
_make(
    "card",
    "djangd/components/card.html",
    defaults={"outlined": False, "media": None, "media_alt": "", "actions": None},
)
_make(
    "paper",
    "djangd/components/paper.html",
    defaults={"elevation": 1},
)
_make(
    "divider",
    "djangd/components/divider.html",
    defaults={"inset": False, "padded": False, "orientation": "horizontal"},
)
_make(
    "elevation",
    "djangd/components/elevation.html",
    defaults={"level": 1},
)

# ---------------------------------------------------------------------------
# Navigation
# ---------------------------------------------------------------------------
_make(
    "app_bar",
    "djangd/components/app_bar.html",
    defaults={
        "title": "",
        "variant": "standard",  # standard | short | short-collapsed | fixed | prominent | dense
        "navigation_icon": "menu",
        "navigation_label": "Open navigation menu",
        "actions": (),
    },
)
_make(
    "drawer",
    "djangd/components/drawer.html",
    defaults={
        "title": "",
        "subtitle": "",
        "variant": "permanent",  # permanent | dismissible | modal
        "open": True,
        "items": (),
    },
)
_make(
    "tab_bar",
    "djangd/components/tab_bar.html",
    defaults={"tabs": (), "active": 0, "stacked": False, "min_width": False},
    required=("tabs",),
)
_make(
    "bottom_navigation",
    "djangd/components/bottom_navigation.html",
    defaults={"items": (), "active": 0},
    required=("items",),
)
_make(
    "menu",
    "djangd/components/menu.html",
    defaults={"items": (), "open": False, "id": None},
    required=("items",),
)
_make(
    "breadcrumbs",
    "djangd/components/breadcrumbs.html",
    defaults={"items": (), "separator": "/"},
    required=("items",),
)
_make(
    "pagination",
    "djangd/components/pagination.html",
    defaults={"page": 1, "total": 1, "url": "?page="},
)

# ---------------------------------------------------------------------------
# Data display
# ---------------------------------------------------------------------------
_make(
    "list",
    "djangd/components/list.html",
    defaults={"items": (), "two_line": False, "avatar_list": False, "dense": False, "non_interactive": False},
    required=("items",),
)
_make(
    "table",
    "djangd/components/table.html",
    defaults={"columns": (), "rows": (), "caption": "", "sticky_header": False},
    required=("columns", "rows"),
)
_make(
    "avatar",
    "djangd/components/avatar.html",
    defaults={"src": None, "alt": "", "initials": "", "size": "medium", "shape": "circle"},
)
_make(
    "badge",
    "djangd/components/badge.html",
    defaults={"value": "", "max": 99, "dot": False, "color": "primary"},
)
_make(
    "tooltip",
    "djangd/components/tooltip.html",
    defaults={"text": "", "id": None, "position": "top"},
    required=("text",),
)
_make(
    "typography",
    "djangd/components/typography.html",
    defaults={"variant": "body1", "tag": None, "text": "", "align": None, "color": None, "no_wrap": False},
)

# ---------------------------------------------------------------------------
# Feedback
# ---------------------------------------------------------------------------
_make(
    "alert",
    "djangd/components/alert.html",
    defaults={"severity": "info", "title": "", "message": "", "dismissible": False, "icon": None},
)
_make(
    "snackbar",
    "djangd/components/snackbar.html",
    defaults={"message": "", "action_label": "", "leading": False, "stacked": False, "id": None},
    required=("message",),
)
_make(
    "dialog",
    "djangd/components/dialog.html",
    defaults={"title": "", "scrim_click_action": "close", "escape_key_action": "close", "actions": (), "id": None},
)
_make(
    "linear_progress",
    "djangd/components/linear_progress.html",
    defaults={"value": None, "buffer": None, "indeterminate": True, "label": "Loading"},
)
_make(
    "circular_progress",
    "djangd/components/circular_progress.html",
    defaults={"value": None, "indeterminate": True, "label": "Loading", "size": "medium"},
)
_make(
    "skeleton",
    "djangd/components/skeleton.html",
    defaults={"variant": "text", "width": None, "height": None, "lines": 1, "animation": "pulse"},
)

# ---------------------------------------------------------------------------
# Misc / utility
# ---------------------------------------------------------------------------
_make(
    "icon",
    "djangd/components/icon.html",
    defaults={"name": "", "label": "", "size": None},
    required=("name",),
)
_make(
    "image_list",
    "djangd/components/image_list.html",
    defaults={"items": (), "masonry": False, "with_text": False},
    required=("items",),
)
_make(
    "stepper",
    "djangd/components/stepper.html",
    defaults={"steps": (), "active": 0, "orientation": "horizontal"},
    required=("steps",),
)
_make(
    "accordion",
    "djangd/components/accordion.html",
    defaults={"items": (), "exclusive": False},
    required=("items",),
)
_make(
    "speed_dial",
    "djangd/components/speed_dial.html",
    defaults={"icon": "add", "label": "", "actions": ()},
    required=("actions",),
)
_make(
    "rating",
    "djangd/components/rating.html",
    defaults={"value": 0, "max": 5, "readonly": False, "name": "rating", "label": "Rating"},
)
_make(
    "toggle_button_group",
    "djangd/components/toggle_button_group.html",
    defaults={"items": (), "value": None, "name": "toggle", "exclusive": True},
    required=("items",),
)
_make(
    "container",
    "djangd/components/container.html",
    defaults={"max_width": "lg", "fluid": False, "padded": True},
)
_make(
    "grid",
    "djangd/components/grid.html",
    defaults={"columns": 12, "gap": "md", "items": ()},
)
_make(
    "stack",
    "djangd/components/stack.html",
    defaults={"direction": "vertical", "gap": "md", "align": None, "justify": None, "items": ()},
)
_make(
    "box",
    "djangd/components/box.html",
    defaults={
        "tag": "div",
        "padding": None,   # 0..6 | None — maps to djangd-box--p-<n>
        "margin": None,    # 0..6 | "auto" | None — maps to djangd-box--m-<n>
        "display": None,   # block | inline | inline-block | flex | inline-flex | grid | hidden | None
        "align": None,     # start | center | end | stretch | None
        "justify": None,   # start | center | end | between | around | None
        "rounded": None,   # xs | sm | md | lg | pill | None
        "surface": None,   # default | variant | primary | None
        "id": None,
    },
)

# ---------------------------------------------------------------------------
# Inputs (extended): autocomplete, button group, transfer list
# ---------------------------------------------------------------------------
_make(
    "autocomplete",
    "djangd/components/autocomplete.html",
    defaults={
        "label": "",
        "name": "",
        "value": "",
        "options": (),   # iterable of strings, or dicts: {"value": ..., "label": ...}
        "placeholder": "",
        "helper": "",
        "required": False,
        "disabled": False,
        "id": None,
    },
    required=("label", "name"),
)
_make(
    "button_group",
    "djangd/components/button_group.html",
    defaults={
        "buttons": (),       # iterable of pre-rendered button HTML strings
        "label": "",         # accessible group label
        "orientation": "horizontal",  # horizontal | vertical
        "variant": "contained",       # contained | outlined
        "full_width": False,
        "id": None,
    },
)
_make(
    "transfer_list",
    "djangd/components/transfer_list.html",
    defaults={
        "name": "transfer",
        "label": "",
        "source_title": "Available",
        "target_title": "Selected",
        "source_items": (),  # iterable of strings or {"value": ..., "label": ...}
        "target_items": (),  # iterable of strings or {"value": ..., "label": ...}
        "id": None,
    },
)

# ---------------------------------------------------------------------------
# Overlays: backdrop, modal, popover
# ---------------------------------------------------------------------------
_make(
    "backdrop",
    "djangd/components/backdrop.html",
    defaults={"open": False, "invisible": False, "id": None},
)
_make(
    "modal",
    "djangd/components/modal.html",
    defaults={
        "open": False,
        "label": "",
        "labelledby": "",
        "describedby": "",
        "id": None,
    },
)
_make(
    "popover",
    "djangd/components/popover.html",
    defaults={
        "open": False,
        "placement": "bottom",  # top | bottom | left | right
        "anchor": None,         # CSS selector or element id the popover is anchored to
        "arrow": True,
        "label": "",
        "id": None,
    },
)

# ---------------------------------------------------------------------------
# Link
# ---------------------------------------------------------------------------
_make(
    "link",
    "djangd/components/link.html",
    defaults={
        "text": "",
        "href": "#",
        "target": None,        # _self | _blank | _parent | _top | None
        "variant": "body",     # body | button | inherit
        "underline": "always", # always | hover | none
        "color": "primary",    # primary | secondary | error | success | warning | inherit
        "id": None,
    },
    required=("href",),
)

# ---------------------------------------------------------------------------
# Inputs (modern): input_otp, file_upload, toggle, date_picker
# ---------------------------------------------------------------------------
_make(
    "input_otp",
    "djangd/components/input_otp.html",
    defaults={
        "label": "Verification code",
        "name": "otp",
        # Length is controlled by the number of items in `slots`. Each slot's
        # value is rendered into the corresponding <input value="…">.
        "slots": ("", "", "", "", "", ""),
        "mask": False,
        "helper": "",
        "disabled": False,
        "id": None,
    },
    required=("name",),
)
_make(
    "file_upload",
    "djangd/components/file_upload.html",
    defaults={
        "name": "file",
        "title": "Click to upload or drag and drop",
        "hint": "",
        "icon": "cloud_upload",
        "accept": "",
        "multiple": False,
        "required": False,
        "disabled": False,
        "id": None,
    },
    required=("name",),
)
_make(
    "toggle",
    "djangd/components/toggle.html",
    defaults={
        "text": "",
        "icon": None,
        "label": "",        # aria-label for icon-only toggles
        "pressed": False,
        "variant": "ghost", # ghost | outline
        "size": "medium",   # small | medium | large
        "disabled": False,
        "id": None,
    },
)
_make(
    "date_picker",
    "djangd/components/date_picker.html",
    defaults={
        "label": "Date",
        "name": "date",
        "value": "",
        "min_date": "",
        "max_date": "",
        "helper": "",
        "icon": "event",
        "required": False,
        "disabled": False,
        "id": None,
    },
    required=("name",),
)

# ---------------------------------------------------------------------------
# Data display (modern): timeline, tree_view, stat, avatar_group, kbd, status,
# calendar
# ---------------------------------------------------------------------------
_make(
    "timeline",
    "djangd/components/timeline.html",
    defaults={
        "items": (),  # iterable of {time, datetime, title, description, icon, active}
        "orientation": "vertical",  # vertical | horizontal
        "align": "start",           # start | center
        "label": "",
        "id": None,
    },
    required=("items",),
)
_make(
    "tree_view",
    "djangd/components/tree_view.html",
    defaults={
        "nodes": (),  # iterable of {label, icon, expanded, selected, children}
        "label": "",
        "id": None,
    },
    required=("nodes",),
)
_make(
    "stat",
    "djangd/components/stat.html",
    defaults={
        "label": "",
        "value": "",
        "unit": "",
        "delta": "",
        "delta_label": "",
        "trend": "flat",  # up | down | flat
        "icon": None,
        "id": None,
    },
    required=("label", "value"),
)
_make(
    "avatar_group",
    "djangd/components/avatar_group.html",
    defaults={
        "avatars": (),  # iterable of {src, alt, initials}
        "max": 4,
        "size": "medium",   # small | medium | large
        "shape": "circle",  # circle | rounded | square
        "label": "",
        "id": None,
    },
    required=("avatars",),
)
_make(
    "kbd",
    "djangd/components/kbd.html",
    defaults={
        "keys": (),        # iterable of strings — each rendered as a key cap
        "text": "",        # single key shortcut as plain text (alt to `keys`)
        "separator": "+",
        "size": "md",      # sm | md | lg
        "label": "",
        "id": None,
    },
)
_make(
    "status",
    "djangd/components/status.html",
    defaults={
        "text": "",
        "tone": "neutral",  # online | offline | busy | away | success | warning | error | info | neutral
        "pulse": False,
        "label": "",
        "id": None,
    },
)
_make(
    "calendar",
    "djangd/components/calendar.html",
    defaults={
        "month": "",
        "year": "",
        "weekdays": ("Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"),
        # weeks is an iterable of weeks (iterables of cells). Each cell is a
        # mapping: {day, iso, outside, today, selected, disabled}.
        "weeks": (),
        "label": "Calendar",
        "id": None,
    },
    required=("weeks",),
)

# ---------------------------------------------------------------------------
# Overlays (modern): hover_card, sheet, command, empty_state
# ---------------------------------------------------------------------------
_make(
    "hover_card",
    "djangd/components/hover_card.html",
    defaults={
        "trigger": "",          # inline content for the trigger
        "placement": "bottom",  # top | bottom | left | right
        "id": None,
    },
)
_make(
    "sheet",
    "djangd/components/sheet.html",
    defaults={
        "open": False,
        "side": "right",  # left | right | top | bottom
        "title": "",
        "dismissible": True,
        "actions": (),    # iterable of pre-rendered HTML strings
        "id": None,
    },
)
_make(
    "command",
    "djangd/components/command.html",
    defaults={
        "open": False,
        "placeholder": "Type a command or search…",
        "label": "Command palette",
        # groups: iterable of {heading, commands: [{label, icon, shortcut, value}]}
        # NB: `commands` (not `items`) avoids colliding with dict.items() during
        # Django template variable resolution.
        "groups": (),
        "empty": "No results.",
        "id": None,
    },
    required=("groups",),
)
_make(
    "empty_state",
    "djangd/components/empty_state.html",
    defaults={
        "title": "",
        "description": "",
        "icon": "inbox",
        "actions": (),
        "id": None,
    },
)

# ---------------------------------------------------------------------------
# Layout (modern): aspect_ratio, scroll_area, toolbar, carousel, visually_hidden
# ---------------------------------------------------------------------------
_make(
    "aspect_ratio",
    "djangd/components/aspect_ratio.html",
    defaults={"ratio": "16 / 9", "id": None},
)
_make(
    "scroll_area",
    "djangd/components/scroll_area.html",
    defaults={
        "orientation": "vertical",  # vertical | horizontal | both
        "max_height": "",
        "max_width": "",
        "label": "",
        "id": None,
    },
)
_make(
    "toolbar",
    "djangd/components/toolbar.html",
    defaults={
        "items": (),          # iterable of pre-rendered HTML strings
        "density": "regular", # dense | regular | spacious
        "orientation": "horizontal",  # horizontal | vertical
        "elevated": False,
        "label": "",
        "id": None,
    },
)
_make(
    "carousel",
    "djangd/components/carousel.html",
    defaults={
        "slides": (),         # iterable of {image, alt, caption, html}
        "active": 0,
        "controls": True,
        "indicators": True,
        "label": "Carousel",
        "id": None,
    },
    required=("slides",),
)
_make(
    "visually_hidden",
    "djangd/components/visually_hidden.html",
    defaults={"tag": "span", "text": "", "id": None},
)

# ---------------------------------------------------------------------------
# Round 3 — more modern app components: inputs, data, feedback, overlays.
# ---------------------------------------------------------------------------
_make(
    "time_picker",
    "djangd/components/time_picker.html",
    defaults={
        "label": "Time", "name": "time", "value": "",
        "step": 60, "min_time": "", "max_time": "",
        "helper": "", "required": False, "disabled": False, "id": None,
    },
    required=("name",),
)
_make(
    "color_picker",
    "djangd/components/color_picker.html",
    defaults={
        "label": "Colour", "name": "color", "value": "#6750a4",
        "helper": "", "required": False, "disabled": False, "id": None,
    },
    required=("name",),
)
_make(
    "number_field",
    "djangd/components/number_field.html",
    defaults={
        "label": "Number", "name": "qty", "value": 1, "step": 1,
        "min_value": None, "max_value": None, "placeholder": "",
        "helper": "", "required": False, "disabled": False, "id": None,
    },
    required=("name",),
)
_make(
    "search",
    "djangd/components/search.html",
    defaults={
        "label": "Search", "name": "q", "value": "",
        "placeholder": "Search…",
        "action": "", "shortcut": "", "disabled": False, "id": None,
    },
)
_make(
    "password_field",
    "djangd/components/password_field.html",
    defaults={
        "label": "Password", "name": "password", "value": "",
        "placeholder": "", "helper": "",
        "autocomplete": "current-password",
        "minlength": None, "required": False, "disabled": False, "error": False, "id": None,
    },
    required=("name",),
)
_make(
    "tag_input",
    "djangd/components/tag_input.html",
    defaults={
        "label": "Tags", "name": "tags", "tags": (),
        "placeholder": "Add a tag and press Enter",
        "helper": "", "required": False, "disabled": False, "id": None,
    },
    required=("name",),
)
_make(
    "code",
    "djangd/components/code.html",
    defaults={
        "code": "", "language": "text", "title": "",
        "line_numbers": False, "id": None,
    },
)
_make(
    "description_list",
    "djangd/components/description_list.html",
    defaults={
        "items": (),                  # iterable of {term, description}
        "orientation": "horizontal",  # horizontal | vertical
        "id": None,
    },
    required=("items",),
)
_make(
    "profile_card",
    "djangd/components/profile_card.html",
    defaults={
        "name": "", "role": "", "bio": "",
        "avatar": "", "initials": "", "avatar_shape": "circle",
        "status_text": "", "status_tone": "online",
        "outlined": False,
        "actions": (),
        "id": None,
    },
    required=("name",),
)
_make(
    "toast",
    "djangd/components/toast.html",
    defaults={
        "open": False, "tone": "info",   # info | success | warning | error
        "title": "", "message": "",
        "icon": None, "action_label": "", "dismissible": True,
        "id": None,
    },
)
_make(
    "banner",
    "djangd/components/banner.html",
    defaults={
        "tone": "info",   # info | success | warning | error
        "title": "", "message": "",
        "icon": None, "label": "",
        "actions": (), "dismissible": True,
        "id": None,
    },
)
_make(
    "dropdown_menu",
    "djangd/components/dropdown_menu.html",
    defaults={
        "open": False,
        "placement": "bottom",  # bottom | bottom-end | top
        "trigger_label": "Menu",
        "trigger_icon": None,
        "trigger_classes": "",
        # items: iterable of {label, href, icon, shortcut, danger} or
        # {divider: True}.
        "items": (),
        "id": None,
    },
    required=("items",),
)


# ---------------------------------------------------------------------------
# Component metadata: logical group + the SCSS partial(s) each component
# needs. Consumed by the tree-shake settings filter and by the
# ``djangd_build_css`` management command.
#
# Groups: inputs | surfaces | navigation | data | feedback | overlays |
#         layout | utility
# Partials are filenames under ``static/djangd/scss/components/`` without
# the leading underscore or extension (e.g. "button" -> "_button.scss").
# ---------------------------------------------------------------------------
_COMPONENT_META: dict[str, tuple[str, tuple[str, ...]]] = {
    # Inputs
    "button":              ("inputs", ("button",)),
    "icon_button":         ("inputs", ("icon-button",)),
    "fab":                 ("inputs", ("fab",)),
    "chip":                ("inputs", ("chip",)),
    "text_field":          ("inputs", ("text-field",)),
    "checkbox":            ("inputs", ("selection",)),
    "radio":               ("inputs", ("selection",)),
    "switch":              ("inputs", ("selection",)),
    "select":              ("inputs", ("selection",)),
    "slider":              ("inputs", ("selection",)),
    "form_field":          ("inputs", ("selection",)),
    "autocomplete":        ("inputs", ("inputs",)),
    "button_group":        ("inputs", ("inputs", "button")),
    "transfer_list":       ("inputs", ("inputs",)),
    "input_otp":           ("inputs", ("inputs-extras",)),
    "file_upload":         ("inputs", ("inputs-extras",)),
    "toggle":              ("inputs", ("inputs-extras",)),
    "date_picker":         ("inputs", ("inputs-extras",)),
    "rating":              ("inputs", ("layout",)),
    "toggle_button_group": ("inputs", ("layout",)),
    # Surfaces
    "card":                ("surfaces", ("card",)),
    "paper":               ("surfaces", ("layout",)),
    "divider":             ("surfaces", ("layout",)),
    "elevation":           ("surfaces", ("layout",)),
    # Navigation
    "app_bar":             ("navigation", ("navigation",)),
    "drawer":              ("navigation", ("navigation",)),
    "tab_bar":             ("navigation", ("navigation",)),
    "bottom_navigation":   ("navigation", ("navigation",)),
    "menu":                ("navigation", ("navigation",)),
    "breadcrumbs":         ("navigation", ("navigation",)),
    "pagination":          ("navigation", ("navigation",)),
    "link":                ("navigation", ("link",)),
    # Data display
    "list":                ("data", ("data",)),
    "table":               ("data", ("data",)),
    "avatar":              ("data", ("data",)),
    "badge":               ("data", ("data",)),
    "tooltip":             ("data", ("data",)),
    "typography":          ("data", ("data",)),
    "timeline":            ("data", ("data-extras",)),
    "tree_view":           ("data", ("data-extras",)),
    "stat":                ("data", ("data-extras",)),
    "avatar_group":        ("data", ("data", "data-extras")),
    "kbd":                 ("data", ("data-extras",)),
    "status":              ("data", ("data-extras",)),
    "calendar":            ("data", ("data-extras",)),
    "image_list":          ("data", ("layout",)),
    # Feedback
    "alert":               ("feedback", ("feedback",)),
    "snackbar":            ("feedback", ("feedback",)),
    "dialog":              ("feedback", ("feedback",)),
    "linear_progress":     ("feedback", ("feedback",)),
    "circular_progress":   ("feedback", ("feedback",)),
    "skeleton":            ("feedback", ("feedback",)),
    "empty_state":         ("feedback", ("overlays-extras",)),
    # Overlays
    "backdrop":            ("overlays", ("overlays",)),
    "modal":               ("overlays", ("overlays",)),
    "popover":             ("overlays", ("overlays",)),
    "hover_card":          ("overlays", ("overlays-extras",)),
    "sheet":               ("overlays", ("overlays-extras",)),
    "command":             ("overlays", ("overlays-extras", "data-extras")),  # uses kbd
    # Layout
    "container":           ("layout", ("layout",)),
    "grid":                ("layout", ("layout",)),
    "stack":               ("layout", ("layout",)),
    "box":                 ("layout", ("box",)),
    "stepper":             ("layout", ("layout",)),
    "accordion":           ("layout", ("layout",)),
    "speed_dial":          ("layout", ("fab",)),
    "aspect_ratio":        ("layout", ("layout-extras",)),
    "scroll_area":         ("layout", ("layout-extras",)),
    "toolbar":             ("layout", ("layout-extras",)),
    "carousel":            ("layout", ("layout-extras",)),
    # Utility
    "icon":                ("utility", ()),
    "visually_hidden":     ("utility", ()),
    # Round 3 additions
    "time_picker":         ("inputs", ("modern-2",)),
    "color_picker":        ("inputs", ("modern-2",)),
    "number_field":        ("inputs", ("modern-2",)),
    "search":              ("inputs", ("modern-2", "data-extras")),  # uses kbd
    "password_field":      ("inputs", ("modern-2",)),
    "tag_input":           ("inputs", ("modern-2", "chip")),
    "code":                ("data",   ("modern-2",)),
    "description_list":    ("data",   ("modern-2",)),
    "profile_card":        ("data",   ("modern-2", "data", "data-extras")),
    "toast":               ("feedback", ("modern-2",)),
    "banner":              ("feedback", ("modern-2",)),
    "dropdown_menu":       ("overlays", ("modern-2",)),
}

# Apply the metadata to every registered class.
for _name, (_group, _scss) in _COMPONENT_META.items():
    if _name in registry:
        _cls = registry.get(_name)
        _cls.group = _group
        _cls.scss_partials = _scss


# Allow users to opt out of components via Django settings:
#
#     DJANGD_FRAMEWORK = {
#         # Whitelist mode — only these components are kept registered.
#         "INCLUDE_COMPONENTS": ["button", "card", "alert"],
#         # …or groups (any component whose group is in this list is kept).
#         "INCLUDE_GROUPS": ["inputs", "feedback"],
#         # Blacklist mode — everything except these is kept.
#         "EXCLUDE_COMPONENTS": ["carousel", "calendar"],
#         "EXCLUDE_GROUPS": ["overlays"],
#     }
#
# INCLUDE_* and EXCLUDE_* combine: a component is kept iff it passes both the
# include filter (if any) and the exclude filter.
def _apply_settings_filter() -> None:
    try:
        from django.conf import settings
    except Exception:
        return
    config = getattr(settings, "DJANGD_FRAMEWORK", None)
    if not isinstance(config, dict):
        return

    include_components = set(config.get("INCLUDE_COMPONENTS") or [])
    include_groups     = set(config.get("INCLUDE_GROUPS") or [])
    exclude_components = set(config.get("EXCLUDE_COMPONENTS") or [])
    exclude_groups     = set(config.get("EXCLUDE_GROUPS") or [])

    if not (include_components or include_groups or exclude_components or exclude_groups):
        return

    has_include = bool(include_components or include_groups)
    for name in list(registry.all()):
        cls = registry.get(name)
        group = getattr(cls, "group", "misc")
        keep = True
        if has_include:
            keep = name in include_components or group in include_groups
        if keep and (name in exclude_components or group in exclude_groups):
            keep = False
        if not keep:
            registry.unregister(name)


_apply_settings_filter()

