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
  // The framework renders the native <dialog> element. Storybook's
  // sandbox renders it with the `open` attribute (non-modal mode) so
  // it shows in-flow alongside the demo backdrop. In production, call
  // `dialog.showModal()` to promote it to the top layer with a real
  // ::backdrop, focus trap, and Esc-to-dismiss handling.
  render: ({ open, title, body }) => `
  <div style="position:relative;height:320px;border:1px dashed var(--djangd-color-outline);overflow:hidden;">
    <p style="padding:16px;">Page content under the modal.</p>
    ${open ? `<div aria-hidden="true" style="position:absolute;inset:0;background:rgba(0,0,0,.5);"></div>` : ""}
    <dialog class="djangd-modal" ${open ? "open" : ""}
            aria-labelledby="modal-title"
            style="position:absolute;top:50%;left:50%;transform:translate(-50%,-50%);">
      <h2 id="modal-title" style="margin:0 0 8px 0;">${title}</h2>
      <p style="margin:0 0 16px 0;">${body}</p>
      <div style="display:flex;gap:8px;justify-content:flex-end;">
        <button class="mdc-button mdc-button--outlined djangd-button" type="button">Cancel</button>
        <button class="mdc-button mdc-button--raised djangd-button djangd-button--raised" type="button">Confirm</button>
      </div>
    </dialog>
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
