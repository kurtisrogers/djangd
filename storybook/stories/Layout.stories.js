export default { title: "Layout", tags: ["autodocs"] };

export const Grid = {
  render: () => `
  <div class="djangd-grid djangd-grid--cols-12 djangd-grid--gap-md">
    ${Array.from({ length: 12 }, (_, i) =>
      `<div class="djangd-grid__cell"><div class="djangd-paper djangd-paper--elevation-1" style="text-align:center;">${i + 1}</div></div>`
    ).join("")}
  </div>`,
};

export const Stack = {
  render: () => `
  <div class="djangd-stack djangd-stack--horizontal djangd-stack--gap-md djangd-stack--align-center">
    <button class="mdc-button mdc-button--outlined djangd-button">Cancel</button>
    <button class="mdc-button mdc-button--raised djangd-button djangd-button--raised">Save</button>
  </div>`,
};

export const Container = {
  render: () => `
  <div class="djangd-container djangd-container--lg djangd-container--padded" style="background:var(--djangd-color-surface-variant);padding:32px;">
    <p>Centred max-width container with padding.</p>
  </div>`,
};
