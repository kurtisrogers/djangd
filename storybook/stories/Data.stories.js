export default { title: "Data Display", tags: ["autodocs"] };

export const Chip = {
  render: () => `
  <div style="display:flex;gap:8px;flex-wrap:wrap;">
    <div class="mdc-chip djangd-chip" role="row"><span class="mdc-chip__text">Default</span></div>
    <div class="mdc-chip mdc-chip--selected djangd-chip djangd-chip--selected" role="row"><i class="material-icons mdc-chip__icon" aria-hidden="true">check</i><span class="mdc-chip__text">Selected</span></div>
    <div class="mdc-chip djangd-chip" role="row"><span class="mdc-chip__text">Removable</span><button class="mdc-chip__icon mdc-chip__icon--trailing" aria-label="Remove"><i class="material-icons" aria-hidden="true">cancel</i></button></div>
  </div>`,
};

export const Avatar = {
  render: () => `
  <div style="display:flex;gap:12px;align-items:center;">
    <span class="djangd-avatar djangd-avatar--circle djangd-avatar--small"><span class="djangd-avatar__initials">KR</span></span>
    <span class="djangd-avatar djangd-avatar--circle"><span class="djangd-avatar__initials">JD</span></span>
    <span class="djangd-avatar djangd-avatar--circle djangd-avatar--large"><i class="material-icons">person</i></span>
    <span class="djangd-avatar djangd-avatar--rounded djangd-avatar--large"><img class="djangd-avatar__image" src="https://i.pravatar.cc/56" alt=""/></span>
  </div>`,
};

export const Badge = {
  args: { value: 8 },
  render: ({ value }) => `
  <span class="djangd-badge djangd-badge--primary" role="status" aria-label="${value} unread">
    <button class="djangd-icon-button" aria-label="Notifications"><i class="material-icons" aria-hidden="true">notifications</i></button>
    <span class="djangd-badge__content">${value}</span>
  </span>`,
};

export const Typography = {
  render: () => `
  <div style="display:flex;flex-direction:column;gap:8px;">
    <h1 class="djangd-typography djangd-typography--display-medium">Display medium</h1>
    <h2 class="djangd-typography djangd-typography--headline-medium">Headline medium</h2>
    <h3 class="djangd-typography djangd-typography--title-large">Title large</h3>
    <p class="djangd-typography djangd-typography--body-large">Body large copy is used in main content.</p>
    <p class="djangd-typography djangd-typography--body-medium djangd-typography--color-muted">Body medium muted.</p>
  </div>`,
};

export const Table = {
  render: () => `
  <div class="djangd-table mdc-data-table" role="region" aria-label="Sample table">
    <table>
      <thead><tr><th scope="col">Dessert</th><th scope="col">Calories</th><th scope="col" class="mdc-data-table__header-cell--numeric">Fat (g)</th></tr></thead>
      <tbody>
        <tr><td>Frozen yoghurt</td><td>159</td><td class="mdc-data-table__cell--numeric">6.0</td></tr>
        <tr><td>Ice cream sandwich</td><td>237</td><td class="mdc-data-table__cell--numeric">9.0</td></tr>
        <tr><td>Eclair</td><td>262</td><td class="mdc-data-table__cell--numeric">16.0</td></tr>
      </tbody>
    </table>
  </div>`,
};
