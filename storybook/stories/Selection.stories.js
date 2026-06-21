export default { title: "Inputs/Selection", tags: ["autodocs"] };

export const Checkbox = {
  args: { checked: true, label: "I agree to the terms" },
  argTypes: { checked: { control: "boolean" }, label: { control: "text" } },
  render: ({ checked, label }) => `
  <div class="mdc-form-field djangd-form-field">
    <div class="mdc-checkbox djangd-checkbox">
      <input type="checkbox" class="mdc-checkbox__native-control" id="cb1" ${checked ? "checked" : ""} />
      <div class="mdc-checkbox__background">
        <svg class="mdc-checkbox__checkmark" viewBox="0 0 24 24" aria-hidden="true">
          <path class="mdc-checkbox__checkmark-path" d="M1.73,12.91 8.1,19.28 22.79,4.59"/>
        </svg>
      </div>
    </div>
    <label for="cb1">${label}</label>
  </div>`,
};

export const Radio = {
  args: { label: "Option A", checked: true },
  render: ({ label, checked }) => `
  <div class="mdc-form-field"><div class="mdc-radio djangd-radio">
    <input type="radio" name="opt" id="r1" class="mdc-radio__native-control" ${checked ? "checked" : ""} />
    <div class="mdc-radio__background"><div class="mdc-radio__outer-circle"></div><div class="mdc-radio__inner-circle"></div></div>
  </div><label for="r1">${label}</label></div>`,
};

export const Switch = {
  args: { checked: true, label: "Enable notifications" },
  render: ({ checked, label }) => `
  <div class="mdc-form-field djangd-form-field">
    <button class="mdc-switch djangd-switch ${checked ? "mdc-switch--selected" : "mdc-switch--unselected"}"
      role="switch" aria-checked="${checked}" id="sw1" type="button">
      <div class="mdc-switch__track"></div>
      <div class="mdc-switch__handle"></div>
    </button>
    <label for="sw1">${label}</label>
  </div>`,
};
