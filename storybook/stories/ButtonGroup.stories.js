import { cls } from "./_helpers.js";

const btn = (label, variant = "outlined") =>
  `<button class="${cls("mdc-button", "mdc-button--" + variant, "djangd-button", "djangd-button--medium")}"
     type="button">
     <span class="mdc-button__label">${label}</span>
   </button>`;

export default { title: "Inputs/Button Group", tags: ["autodocs"] };

export const Horizontal = {
  args: { variant: "outlined", orientation: "horizontal", fullWidth: false },
  argTypes: {
    variant:     { control: { type: "select" }, options: ["outlined", "contained"] },
    orientation: { control: { type: "select" }, options: ["horizontal", "vertical"] },
    fullWidth:   { control: "boolean" },
  },
  render: ({ variant, orientation, fullWidth }) => `
  <div class="${cls(
    "djangd-button-group",
    "djangd-button-group--" + orientation,
    "djangd-button-group--" + variant,
    fullWidth && "djangd-button-group--full-width"
  )}" role="group" aria-label="Text alignment">
    ${btn("Left", variant === "contained" ? "raised" : "outlined")}
    ${btn("Centre", variant === "contained" ? "raised" : "outlined")}
    ${btn("Right", variant === "contained" ? "raised" : "outlined")}
  </div>`,
};

export const Vertical = { ...Horizontal, args: { ...Horizontal.args, orientation: "vertical" } };
export const Contained = { ...Horizontal, args: { ...Horizontal.args, variant: "contained" } };
