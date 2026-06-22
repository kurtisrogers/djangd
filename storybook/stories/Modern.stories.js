import { cls } from "./_helpers.js";

export default { title: "Modern", tags: ["autodocs"] };

// ---- Inputs -----------------------------------------------------------------

export const InputOtp = {
  name: "Inputs/Input OTP",
  args: { length: 6, mask: false },
  argTypes: {
    length: { control: { type: "number", min: 4, max: 8 } },
    mask:   { control: "boolean" },
  },
  render: ({ length, mask }) => `
  <fieldset class="djangd-input-otp" role="group">
    <legend class="djangd-input-otp__legend">Verification code</legend>
    <div class="djangd-input-otp__slots">
      ${Array.from({ length }, (_, i) =>
        `<input class="djangd-input-otp__slot" type="${mask ? "password" : "text"}"
                inputmode="numeric" autocomplete="one-time-code" maxlength="1"
                aria-label="Digit ${i + 1}" />`
      ).join("")}
    </div>
    <div class="djangd-input-otp__helper">Enter the ${length}-digit code we just sent you.</div>
  </fieldset>`,
};

export const FileUpload = {
  name: "Inputs/File Upload",
  args: { title: "Click to upload or drag and drop", hint: "PNG, JPG up to 5 MB", multiple: false },
  argTypes: {
    title:    { control: "text" },
    hint:     { control: "text" },
    multiple: { control: "boolean" },
  },
  render: ({ title, hint, multiple }) => `
  <label class="djangd-file-upload">
    <input class="djangd-file-upload__input" type="file" ${multiple ? "multiple" : ""} />
    <span class="djangd-file-upload__surface">
      <i class="material-icons djangd-file-upload__icon" aria-hidden="true">cloud_upload</i>
      <span class="djangd-file-upload__title">${title}</span>
      <span class="djangd-file-upload__hint">${hint}</span>
    </span>
  </label>`,
};

export const Toggle = {
  name: "Inputs/Toggle",
  args: { text: "Bold", icon: "format_bold", pressed: true, variant: "ghost", size: "medium" },
  argTypes: {
    text:    { control: "text" },
    icon:    { control: "text" },
    pressed: { control: "boolean" },
    variant: { control: { type: "select" }, options: ["ghost", "outline"] },
    size:    { control: { type: "select" }, options: ["small", "medium", "large"] },
  },
  render: ({ text, icon, pressed, variant, size }) => `
  <button class="${cls("djangd-toggle", "djangd-toggle--" + variant, "djangd-toggle--" + size, pressed && "djangd-toggle--on")}"
          type="button" aria-pressed="${pressed}">
    ${icon ? `<i class="material-icons djangd-toggle__icon" aria-hidden="true">${icon}</i>` : ""}
    ${text ? `<span class="djangd-toggle__label">${text}</span>` : ""}
  </button>`,
};

export const DatePicker = {
  name: "Inputs/Date Picker",
  args: { label: "Departure date", value: "2026-09-01", helper: "" },
  argTypes: { label: { control: "text" }, value: { control: "text" }, helper: { control: "text" } },
  render: ({ label, value, helper }) => `
  <div class="djangd-date-picker">
    <label class="djangd-date-picker__label" for="dp">${label}</label>
    <div class="djangd-date-picker__field">
      <input class="djangd-date-picker__input mdc-text-field__input" id="dp" type="date" value="${value}" />
      <i class="material-icons djangd-date-picker__icon" aria-hidden="true">event</i>
    </div>
    ${helper ? `<div class="djangd-date-picker__helper">${helper}</div>` : ""}
  </div>`,
};

// ---- Data display -----------------------------------------------------------

export const Timeline = {
  name: "Data/Timeline",
  render: () => `
  <ol class="djangd-timeline djangd-timeline--vertical">
    ${[
      ["Order placed",   "Today 10:42", "We've received your order.", "shopping_cart", true],
      ["Payment confirmed", "Today 10:43", "Your card has been charged.", "credit_card", true],
      ["Shipped",        "Tomorrow",    "Royal Mail tracked 24h.",    "local_shipping", false],
      ["Delivered",      "Friday",      "Signature required at door.","check_circle",   false],
    ].map(([title, time, desc, icon, active]) => `
      <li class="djangd-timeline__item ${active ? "djangd-timeline__item--active" : ""}">
        <div class="djangd-timeline__marker"><i class="material-icons" aria-hidden="true">${icon}</i></div>
        <div class="djangd-timeline__content">
          <time class="djangd-timeline__time">${time}</time>
          <div class="djangd-timeline__title">${title}</div>
          <div class="djangd-timeline__description">${desc}</div>
        </div>
      </li>`).join("")}
  </ol>`,
};

const treeNode = (node, level = 1) => `
  <li class="djangd-tree-view__item ${node.expanded ? "djangd-tree-view__item--expanded" : ""} ${node.selected ? "djangd-tree-view__item--selected" : ""}"
      role="treeitem" aria-level="${level}"
      ${node.children ? `aria-expanded="${!!node.expanded}"` : ""}>
    <div class="djangd-tree-view__row">
      ${node.children
        ? `<button type="button" class="djangd-tree-view__chevron"><i class="material-icons" aria-hidden="true">${node.expanded ? "expand_more" : "chevron_right"}</i></button>`
        : `<span class="djangd-tree-view__chevron djangd-tree-view__chevron--leaf"></span>`}
      ${node.icon ? `<i class="material-icons djangd-tree-view__icon" aria-hidden="true">${node.icon}</i>` : ""}
      <span class="djangd-tree-view__label">${node.label}</span>
    </div>
    ${node.children ? `<ul class="djangd-tree-view__group" role="group">${node.children.map((c) => treeNode(c, level + 1)).join("")}</ul>` : ""}
  </li>`;

export const TreeView = {
  name: "Data/Tree View",
  render: () => `
  <ul class="djangd-tree-view" role="tree">
    ${treeNode({
      label: "src", icon: "folder", expanded: true,
      children: [
        { label: "components", icon: "folder", expanded: true, children: [
          { label: "Button.tsx", icon: "description" },
          { label: "Card.tsx", icon: "description", selected: true },
        ]},
        { label: "utils", icon: "folder", children: [
          { label: "format.ts", icon: "description" },
        ]},
        { label: "index.ts", icon: "description" },
      ],
    })}
  </ul>`,
};

export const Stat = {
  name: "Data/Stat",
  args: { label: "Monthly revenue", value: "£28,420", delta: "+12%", trend: "up" },
  argTypes: {
    label: { control: "text" },
    value: { control: "text" },
    delta: { control: "text" },
    trend: { control: { type: "select" }, options: ["up", "down", "flat"] },
  },
  render: ({ label, value, delta, trend }) => `
  <div style="display:flex;gap:16px;">
    <div class="djangd-stat djangd-stat--${trend}">
      <div class="djangd-stat__icon"><i class="material-icons" aria-hidden="true">paid</i></div>
      <div class="djangd-stat__body">
        <div class="djangd-stat__label">${label}</div>
        <div class="djangd-stat__value">${value}</div>
        <div class="djangd-stat__delta">
          ${trend === "up" ? `<i class="material-icons">arrow_upward</i>` : ""}
          ${trend === "down" ? `<i class="material-icons">arrow_downward</i>` : ""}
          <span>${delta}</span>
          <span class="djangd-stat__delta-label">vs last month</span>
        </div>
      </div>
    </div>
  </div>`,
};

export const AvatarGroup = {
  name: "Data/Avatar Group",
  render: () => `
  <div class="djangd-avatar-group djangd-avatar-group--medium">
    <div class="djangd-avatar djangd-avatar--medium djangd-avatar--circle djangd-avatar-group__item"><span class="djangd-avatar__initials">KR</span></div>
    <div class="djangd-avatar djangd-avatar--medium djangd-avatar--circle djangd-avatar-group__item"><span class="djangd-avatar__initials">JD</span></div>
    <div class="djangd-avatar djangd-avatar--medium djangd-avatar--circle djangd-avatar-group__item"><span class="djangd-avatar__initials">AB</span></div>
    <div class="djangd-avatar djangd-avatar--medium djangd-avatar--circle djangd-avatar-group__item"><span class="djangd-avatar__initials">SR</span></div>
    <div class="djangd-avatar djangd-avatar--medium djangd-avatar--circle djangd-avatar-group__item djangd-avatar-group__overflow"><span class="djangd-avatar__initials">+3</span></div>
  </div>`,
};

export const Kbd = {
  name: "Data/Kbd",
  render: () => `
  <div style="display:flex;flex-direction:column;gap:8px;font-family:var(--djangd-font-family);">
    <div>Open palette: <kbd class="djangd-kbd"><span class="djangd-kbd__key">⌘</span><span class="djangd-kbd__sep">+</span><span class="djangd-kbd__key">K</span></kbd></div>
    <div>Save: <kbd class="djangd-kbd djangd-kbd--sm"><span class="djangd-kbd__key">Ctrl</span><span class="djangd-kbd__sep">+</span><span class="djangd-kbd__key">S</span></kbd></div>
    <div>Send: <kbd class="djangd-kbd djangd-kbd--lg"><span class="djangd-kbd__key">⌘</span><span class="djangd-kbd__sep">+</span><span class="djangd-kbd__key">Enter</span></kbd></div>
  </div>`,
};

export const Status = {
  name: "Data/Status",
  render: () => `
  <div style="display:flex;flex-direction:column;gap:8px;">
    <span class="djangd-status djangd-status--online"><span class="djangd-status__dot"></span><span class="djangd-status__text">Online</span></span>
    <span class="djangd-status djangd-status--away djangd-status--pulse"><span class="djangd-status__dot"></span><span class="djangd-status__text">Away</span></span>
    <span class="djangd-status djangd-status--busy"><span class="djangd-status__dot"></span><span class="djangd-status__text">Do not disturb</span></span>
    <span class="djangd-status djangd-status--offline"><span class="djangd-status__dot"></span><span class="djangd-status__text">Offline</span></span>
  </div>`,
};

export const Calendar = {
  name: "Data/Calendar",
  render: () => {
    const days = [
      [27, 28, 29, 30, 31, 1, 2],
      [3, 4, 5, 6, 7, 8, 9],
      [10, 11, 12, 13, 14, 15, 16],
      [17, 18, 19, 20, 21, 22, 23],
      [24, 25, 26, 27, 28, 29, 30],
      [31, 1, 2, 3, 4, 5, 6],
    ];
    return `
    <div class="djangd-calendar">
      <header class="djangd-calendar__header">
        <button type="button" class="djangd-icon-button mdc-icon-button djangd-calendar__nav" aria-label="Previous month"><i class="material-icons">chevron_left</i></button>
        <h3 class="djangd-calendar__title">August 2026</h3>
        <button type="button" class="djangd-icon-button mdc-icon-button djangd-calendar__nav" aria-label="Next month"><i class="material-icons">chevron_right</i></button>
      </header>
      <table class="djangd-calendar__grid" role="grid">
        <thead><tr role="row">${["Sun","Mon","Tue","Wed","Thu","Fri","Sat"].map((d) => `<th class="djangd-calendar__weekday" scope="col">${d.slice(0, 2)}</th>`).join("")}</tr></thead>
        <tbody>
          ${days.map((week, wi) => `<tr role="row">${
            week.map((day, di) => {
              const outside = (wi === 0 && day > 7) || (wi === 5 && day < 7);
              const today = day === 15 && !outside;
              const selected = day === 21 && !outside;
              return `<td role="gridcell" class="djangd-calendar__cell ${outside ? "djangd-calendar__cell--outside" : ""} ${today ? "djangd-calendar__cell--today" : ""} ${selected ? "djangd-calendar__cell--selected" : ""}">
                <button type="button" class="djangd-calendar__day">${day}</button>
              </td>`;
            }).join("")
          }</tr>`).join("")}
        </tbody>
      </table>
    </div>`;
  },
};

// ---- Overlays ---------------------------------------------------------------

export const HoverCard = {
  name: "Overlays/Hover Card",
  render: () => `
  <p style="font-family:var(--djangd-font-family);max-width:60ch;">
    Click the
    <span class="djangd-hover-card">
      <span class="djangd-hover-card__trigger" tabindex="0">@kurtisrogers</span>
      <span class="djangd-hover-card__panel djangd-hover-card__panel--bottom">
        <span class="djangd-hover-card__surface">
          <strong>Kurtis Rogers</strong><br/>
          Building djangd-framework.<br/>
          <small style="color:var(--djangd-color-on-surface-variant);">Joined Jun 2026 — UK</small>
        </span>
      </span>
    </span>
    handle to see a quick profile card.
  </p>`,
};

export const Sheet = {
  name: "Overlays/Sheet",
  args: { open: true, side: "right" },
  argTypes: {
    open: { control: "boolean" },
    side: { control: { type: "select" }, options: ["left", "right", "top", "bottom"] },
  },
  render: ({ open, side }) => `
  <div style="position:relative;height:360px;border:1px dashed var(--djangd-color-outline);overflow:hidden;">
    <p style="padding:16px;">Page content beneath the sheet.</p>
    <div class="djangd-sheet djangd-sheet--${side} ${open ? "djangd-sheet--open" : ""}" role="dialog" aria-modal="true" style="position:absolute;inset:0;">
      <div class="djangd-sheet__scrim"></div>
      <aside class="djangd-sheet__panel" tabindex="-1">
        <header class="djangd-sheet__header">
          <h2 class="djangd-sheet__title">Filters</h2>
          <button type="button" class="djangd-icon-button mdc-icon-button djangd-sheet__close"><i class="material-icons">close</i></button>
        </header>
        <div class="djangd-sheet__body">
          <p>Configure your view from here. This panel scrolls when content overflows.</p>
        </div>
        <footer class="djangd-sheet__footer">
          <button class="mdc-button mdc-button--outlined djangd-button">Reset</button>
          <button class="mdc-button mdc-button--raised djangd-button djangd-button--raised">Apply</button>
        </footer>
      </aside>
    </div>
  </div>`,
};

export const Command = {
  name: "Overlays/Command Palette",
  args: { open: true },
  argTypes: { open: { control: "boolean" } },
  render: ({ open }) => `
  <div style="position:relative;height:420px;border:1px dashed var(--djangd-color-outline);overflow:hidden;background:var(--djangd-color-background);">
    <p style="padding:16px;">Press <kbd class="djangd-kbd"><span class="djangd-kbd__key">⌘</span><span class="djangd-kbd__sep">+</span><span class="djangd-kbd__key">K</span></kbd> to open.</p>
    <div class="djangd-command ${open ? "djangd-command--open" : ""}" role="dialog" aria-modal="true" style="position:absolute;inset:0;">
      <div class="djangd-command__scrim"></div>
      <div class="djangd-command__panel">
        <div class="djangd-command__searchbar">
          <i class="material-icons djangd-command__search-icon">search</i>
          <input class="djangd-command__input" type="text" placeholder="Type a command or search…" />
          <kbd class="djangd-kbd djangd-kbd--sm djangd-command__hint">Esc</kbd>
        </div>
        <ul class="djangd-command__list">
          <li class="djangd-command__heading">Navigation</li>
          <li class="djangd-command__option" aria-selected="true"><i class="material-icons djangd-command__icon">home</i><span class="djangd-command__label">Go to dashboard</span><kbd class="djangd-kbd djangd-kbd--sm">G D</kbd></li>
          <li class="djangd-command__option"><i class="material-icons djangd-command__icon">person</i><span class="djangd-command__label">Open profile</span><kbd class="djangd-kbd djangd-kbd--sm">G P</kbd></li>
          <li class="djangd-command__heading">Actions</li>
          <li class="djangd-command__option"><i class="material-icons djangd-command__icon">add</i><span class="djangd-command__label">Create new project</span><kbd class="djangd-kbd djangd-kbd--sm">N P</kbd></li>
          <li class="djangd-command__option"><i class="material-icons djangd-command__icon">share</i><span class="djangd-command__label">Share workspace</span></li>
        </ul>
      </div>
    </div>
  </div>`,
};

export const EmptyState = {
  name: "Overlays/Empty State",
  args: { title: "No invoices yet", description: "Create your first invoice to start tracking payments." },
  argTypes: { title: { control: "text" }, description: { control: "text" } },
  render: ({ title, description }) => `
  <div class="djangd-empty-state">
    <div class="djangd-empty-state__icon"><i class="material-icons" aria-hidden="true">receipt_long</i></div>
    <h3 class="djangd-empty-state__title">${title}</h3>
    <p class="djangd-empty-state__description">${description}</p>
    <div class="djangd-empty-state__actions">
      <button class="mdc-button mdc-button--outlined djangd-button">Import</button>
      <button class="mdc-button mdc-button--raised djangd-button djangd-button--raised">Create invoice</button>
    </div>
  </div>`,
};

// ---- Layout / utility -------------------------------------------------------

export const AspectRatio = {
  name: "Layout/Aspect Ratio",
  args: { ratio: "16 / 9" },
  argTypes: { ratio: { control: { type: "select" }, options: ["16 / 9", "4 / 3", "1 / 1", "3 / 4", "21 / 9"] } },
  render: ({ ratio }) => `
  <div class="djangd-aspect-ratio" style="aspect-ratio: ${ratio}; max-width:480px; background:var(--djangd-color-surface-variant); border-radius:var(--djangd-radius-md); display:flex; align-items:center; justify-content:center; color:var(--djangd-color-on-surface-variant);">
    ${ratio}
  </div>`,
};

export const ScrollArea = {
  name: "Layout/Scroll Area",
  render: () => `
  <div class="djangd-scroll-area djangd-scroll-area--vertical" style="max-height:200px;max-width:360px;" tabindex="0">
    <div class="djangd-scroll-area__viewport">
      ${Array.from({ length: 25 }, (_, i) => `<p style="margin:8px 0;">Item ${i + 1} — a long row inside a scrollable container with themed scrollbars.</p>`).join("")}
    </div>
  </div>`,
};

export const Toolbar = {
  name: "Layout/Toolbar",
  args: { density: "regular", elevated: true },
  argTypes: {
    density:  { control: { type: "select" }, options: ["dense", "regular", "spacious"] },
    elevated: { control: "boolean" },
  },
  render: ({ density, elevated }) => `
  <div class="${cls("djangd-toolbar", "djangd-toolbar--" + density, elevated && "djangd-toolbar--elevated")}" role="toolbar" aria-label="Editor toolbar">
    <button class="djangd-icon-button mdc-icon-button" aria-label="Bold"><i class="material-icons">format_bold</i></button>
    <button class="djangd-icon-button mdc-icon-button" aria-label="Italic"><i class="material-icons">format_italic</i></button>
    <button class="djangd-icon-button mdc-icon-button" aria-label="Underline"><i class="material-icons">format_underlined</i></button>
    <span class="djangd-divider djangd-divider--vertical" style="width:1px;height:24px;background:var(--djangd-color-outline);"></span>
    <button class="djangd-icon-button mdc-icon-button" aria-label="Bulleted list"><i class="material-icons">format_list_bulleted</i></button>
    <button class="djangd-icon-button mdc-icon-button" aria-label="Numbered list"><i class="material-icons">format_list_numbered</i></button>
  </div>`,
};

export const Carousel = {
  name: "Layout/Carousel",
  render: () => `
  <section class="djangd-carousel" aria-roledescription="carousel" aria-label="Featured photos" style="max-width:560px;">
    <div class="djangd-carousel__viewport">
      <ul class="djangd-carousel__track" role="list" style="transform: translateX(0%);">
        ${[
          { bg: "#6750a4", t: "Aurora" },
          { bg: "#7d5260", t: "Solstice" },
          { bg: "#2e7d32", t: "Borealis" },
        ].map((s, i) => `
          <li class="djangd-carousel__slide ${i === 0 ? "djangd-carousel__slide--active" : ""}" aria-roledescription="slide">
            <div style="height:280px;background:${s.bg};color:#fff;display:flex;align-items:end;justify-content:flex-start;padding:24px;">
              <div class="djangd-carousel__caption">${s.t}</div>
            </div>
          </li>`).join("")}
      </ul>
    </div>
    <button type="button" class="djangd-icon-button mdc-icon-button djangd-carousel__control djangd-carousel__control--prev" aria-label="Previous"><i class="material-icons">chevron_left</i></button>
    <button type="button" class="djangd-icon-button mdc-icon-button djangd-carousel__control djangd-carousel__control--next" aria-label="Next"><i class="material-icons">chevron_right</i></button>
    <div class="djangd-carousel__indicators" role="tablist">
      <button class="djangd-carousel__indicator djangd-carousel__indicator--active" role="tab" aria-selected="true" aria-label="Slide 1"><span class="djangd-carousel__indicator-dot" aria-hidden="true"></span></button>
      <button class="djangd-carousel__indicator" role="tab" aria-selected="false" aria-label="Slide 2"><span class="djangd-carousel__indicator-dot" aria-hidden="true"></span></button>
      <button class="djangd-carousel__indicator" role="tab" aria-selected="false" aria-label="Slide 3"><span class="djangd-carousel__indicator-dot" aria-hidden="true"></span></button>
    </div>
  </section>`,
};

export const VisuallyHidden = {
  name: "Layout/Visually Hidden",
  render: () => `
  <button class="mdc-button mdc-button--outlined djangd-button" type="button">
    <i class="material-icons" aria-hidden="true">delete</i>
    <span class="djangd-visually-hidden">Delete item</span>
  </button>
  <p style="margin-top:8px;font-family:var(--djangd-font-family);color:var(--djangd-color-on-surface-variant);">
    Icon-only button with a screen-reader-only label.
  </p>`,
};
