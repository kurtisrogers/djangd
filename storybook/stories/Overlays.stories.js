export default { title: "Feedback/Overlays", tags: ["autodocs"] };

export const Backdrop = {
  args: { open: true, invisible: false },
  argTypes: {
    open:      { control: "boolean" },
    invisible: { control: "boolean" },
  },
  render: ({ open, invisible }) => `
  <div style="position:relative;height:240px;border:1px dashed var(--djangd-color-outline);">
    <p style="padding:16px;">Page content under the backdrop.</p>
    <div class="djangd-backdrop ${open ? "djangd-backdrop--open" : ""} ${invisible ? "djangd-backdrop--invisible" : ""}"
         role="presentation" aria-hidden="${!open}" style="position:absolute;">
      <div class="djangd-paper djangd-paper--elevation-3" style="padding:16px;background:var(--djangd-color-surface);color:var(--djangd-color-on-surface);">
        Loading…
      </div>
    </div>
  </div>`,
};

export const Modal = {
  args: { open: true, title: "Confirm action", body: "Are you sure you want to continue?" },
  argTypes: {
    open:  { control: "boolean" },
    title: { control: "text" },
    body:  { control: "text" },
  },
  render: ({ open, title, body }) => `
  <div style="position:relative;height:320px;border:1px dashed var(--djangd-color-outline);">
    <p style="padding:16px;">Page content under the modal.</p>
    <div class="djangd-modal ${open ? "djangd-modal--open" : ""}" role="presentation" aria-hidden="${!open}" style="position:absolute;inset:0;">
      <div class="djangd-modal__backdrop"></div>
      <div class="djangd-modal__container" role="dialog" aria-modal="true" aria-labelledby="modal-title" tabindex="-1">
        <div class="djangd-paper djangd-paper--elevation-3" style="background:var(--djangd-color-surface);color:var(--djangd-color-on-surface);padding:24px;border-radius:var(--djangd-radius-lg);max-width:420px;width:100%;">
          <h2 id="modal-title" style="margin:0 0 8px 0;">${title}</h2>
          <p style="margin:0 0 16px 0;">${body}</p>
          <div style="display:flex;gap:8px;justify-content:flex-end;">
            <button class="mdc-button mdc-button--outlined djangd-button">Cancel</button>
            <button class="mdc-button mdc-button--raised djangd-button djangd-button--raised">Confirm</button>
          </div>
        </div>
      </div>
    </div>
  </div>`,
};

export const Popover = {
  args: { open: true, placement: "bottom", body: "Quick info goes here." },
  argTypes: {
    open:      { control: "boolean" },
    placement: { control: { type: "select" }, options: ["top", "bottom", "left", "right"] },
    body:      { control: "text" },
  },
  render: ({ open, placement, body }) => `
  <div style="position:relative;height:180px;padding:60px;">
    <button class="mdc-button mdc-button--raised djangd-button djangd-button--raised">Trigger</button>
    <div class="djangd-popover djangd-popover--${placement} ${open ? "djangd-popover--open" : ""}"
         role="dialog" aria-hidden="${!open}" style="top:${placement === "top" ? "0" : "70px"};left:60px;">
      <div class="djangd-popover__surface">
        <span class="djangd-popover__arrow" aria-hidden="true"></span>
        <div class="djangd-popover__content">${body}</div>
      </div>
    </div>
  </div>`,
};
