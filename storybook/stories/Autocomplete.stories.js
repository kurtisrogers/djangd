export default { title: "Inputs/Autocomplete", tags: ["autodocs"] };

const OPTIONS = ["Aurora", "Borealis", "Cascade", "Drift", "Eclipse", "Fjord"];

export const Default = {
  args: { label: "City", placeholder: "Start typing…", helper: "Suggestions appear as you type" },
  argTypes: {
    label:       { control: "text" },
    placeholder: { control: "text" },
    helper:      { control: "text" },
    disabled:    { control: "boolean" },
  },
  render: ({ label, placeholder, helper, disabled }) => `
  <div class="djangd-autocomplete ${disabled ? "djangd-autocomplete--disabled" : ""}"
       role="combobox" aria-haspopup="listbox" aria-owns="ac-list" aria-expanded="false">
    <label class="djangd-autocomplete__label" for="ac-input">${label}</label>
    <input class="djangd-autocomplete__input mdc-text-field__input" id="ac-input"
           type="text" role="searchbox" aria-controls="ac-list"
           autocomplete="off" list="ac-datalist" placeholder="${placeholder}"
           ${disabled ? "disabled aria-disabled='true'" : ""} />
    <datalist id="ac-datalist">
      ${OPTIONS.map((o) => `<option value="${o}"></option>`).join("")}
    </datalist>
    <ul class="djangd-autocomplete__listbox" id="ac-list" role="listbox" hidden>
      ${OPTIONS.map((o) => `<li class="djangd-autocomplete__option" role="option">${o}</li>`).join("")}
    </ul>
    ${helper ? `<div class="djangd-autocomplete__helper">${helper}</div>` : ""}
  </div>`,
};

export const OpenListbox = {
  args: { label: "Currency" },
  render: ({ label }) => `
  <div class="djangd-autocomplete" role="combobox" aria-expanded="true" aria-owns="ac-list2">
    <label class="djangd-autocomplete__label" for="ac-input2">${label}</label>
    <input class="djangd-autocomplete__input mdc-text-field__input" id="ac-input2" type="text" value="Eu" />
    <ul class="djangd-autocomplete__listbox" id="ac-list2" role="listbox">
      <li class="djangd-autocomplete__option" role="option" aria-selected="true">EUR — Euro</li>
      <li class="djangd-autocomplete__option" role="option">GBP — British Pound</li>
      <li class="djangd-autocomplete__option" role="option">USD — US Dollar</li>
    </ul>
  </div>`,
};

export const Disabled = { ...Default, args: { ...Default.args, disabled: true } };
