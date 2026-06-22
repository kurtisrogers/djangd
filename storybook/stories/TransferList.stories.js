export default { title: "Inputs/Transfer List", tags: ["autodocs"] };

const ITEMS_LEFT  = ["Alpha", "Bravo", "Charlie", "Delta", "Echo"];
const ITEMS_RIGHT = ["Foxtrot", "Golf"];

const panel = (title, items, selected) => `
  <div class="djangd-transfer-list__panel">
    <div class="djangd-transfer-list__title">${title}</div>
    <ul class="djangd-transfer-list__items" role="listbox" aria-multiselectable="true" aria-label="${title}">
      ${items.map(
        (it) => `
        <li class="djangd-transfer-list__item" role="option" tabindex="0">
          <input type="checkbox" class="djangd-transfer-list__checkbox" ${selected ? "checked" : ""} aria-label="${it}" />
          <span class="djangd-transfer-list__label">${it}</span>
        </li>`
      ).join("")}
    </ul>
  </div>`;

export const Default = {
  render: () => `
  <div class="djangd-transfer-list" role="group" aria-label="Roles">
    ${panel("Available", ITEMS_LEFT, false)}
    <div class="djangd-transfer-list__controls" role="group" aria-label="Transfer controls">
      <button type="button" class="djangd-icon-button mdc-icon-button djangd-transfer-list__move" aria-label="Move all right">
        <i class="material-icons" aria-hidden="true">last_page</i>
      </button>
      <button type="button" class="djangd-icon-button mdc-icon-button djangd-transfer-list__move" aria-label="Move right">
        <i class="material-icons" aria-hidden="true">chevron_right</i>
      </button>
      <button type="button" class="djangd-icon-button mdc-icon-button djangd-transfer-list__move" aria-label="Move left">
        <i class="material-icons" aria-hidden="true">chevron_left</i>
      </button>
      <button type="button" class="djangd-icon-button mdc-icon-button djangd-transfer-list__move" aria-label="Move all left">
        <i class="material-icons" aria-hidden="true">first_page</i>
      </button>
    </div>
    ${panel("Selected", ITEMS_RIGHT, true)}
  </div>`,
};
