const render = ({ label, variant, value, helper, error, required, disabled }) => `
<label class="mdc-text-field mdc-text-field--${variant} djangd-text-field
  ${error ? "mdc-text-field--invalid" : ""} ${disabled ? "mdc-text-field--disabled" : ""}">
  <span class="mdc-floating-label">${label}${required ? " *" : ""}</span>
  <input class="mdc-text-field__input" type="text" value="${value}" ${required ? "required" : ""} ${disabled ? "disabled" : ""} aria-invalid="${error}"/>
</label>
${helper ? `<div class="mdc-text-field-helper-line"><span class="mdc-text-field-helper-text ${error ? "mdc-text-field-helper-text--validation-msg" : ""}">${helper}</span></div>` : ""}`;

export default {
  title: "Inputs/Text Field",
  tags: ["autodocs"],
  render,
  argTypes: {
    variant: { control: "select", options: ["filled", "outlined"] },
    label:   { control: "text" },
    value:   { control: "text" },
    helper:  { control: "text" },
    error:   { control: "boolean" },
    required:{ control: "boolean" },
    disabled:{ control: "boolean" },
  },
  args: { label: "Email", variant: "filled", value: "", helper: "We never share your email.", error: false, required: true, disabled: false },
};

export const Filled    = {};
export const Outlined  = { args: { variant: "outlined" } };
export const WithError = { args: { error: true, helper: "Email is required" } };
export const Disabled  = { args: { disabled: true } };
