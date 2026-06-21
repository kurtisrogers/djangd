import { cls } from "./_helpers.js";

const render = ({ label, variant, size, disabled, icon, href }) => {
  const tag = href ? "a" : "button";
  const Tag = (props, kids) =>
    `<${tag} class="${cls("mdc-button", "mdc-button--" + variant, "djangd-button", "djangd-button--" + size)}"
       ${href ? `href="${href}"` : `type="button"`} ${disabled ? "disabled aria-disabled='true'" : ""}>
       ${icon ? `<i class="material-icons mdc-button__icon" aria-hidden="true">${icon}</i>` : ""}
       <span class="mdc-button__label">${label}</span>
     </${tag}>`;
  return Tag();
};

export default {
  title: "Inputs/Button",
  tags: ["autodocs"],
  render,
  argTypes: {
    label:    { control: "text" },
    variant:  { control: { type: "select" }, options: ["text", "outlined", "raised", "unelevated"] },
    size:     { control: { type: "select" }, options: ["small", "medium", "large"] },
    icon:     { control: "text" },
    href:     { control: "text" },
    disabled: { control: "boolean" },
  },
  args: { label: "Save changes", variant: "raised", size: "medium", disabled: false, icon: "" },
};

export const Raised     = {};
export const Outlined   = { args: { variant: "outlined" } };
export const Text       = { args: { variant: "text", label: "Cancel" } };
export const WithIcon   = { args: { icon: "save" } };
export const AsLink     = { args: { href: "#", label: "Read docs" } };
export const Disabled   = { args: { disabled: true } };
