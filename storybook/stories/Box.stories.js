import { cls } from "./_helpers.js";

export default { title: "Layout/Box", tags: ["autodocs"] };

export const Default = {
  args: { padding: "4", surface: "variant", rounded: "md", display: "block" },
  argTypes: {
    padding: { control: { type: "select" }, options: ["", "0", "1", "2", "3", "4", "5", "6"] },
    margin:  { control: { type: "select" }, options: ["", "0", "1", "2", "3", "4", "5", "6", "auto"] },
    display: { control: { type: "select" }, options: ["", "block", "inline-block", "flex", "inline-flex", "grid"] },
    align:   { control: { type: "select" }, options: ["", "start", "center", "end", "stretch"] },
    justify: { control: { type: "select" }, options: ["", "start", "center", "end", "between", "around"] },
    rounded: { control: { type: "select" }, options: ["", "xs", "sm", "md", "lg", "pill"] },
    surface: { control: { type: "select" }, options: ["", "default", "variant", "primary"] },
  },
  render: ({ padding, margin, display, align, justify, rounded, surface }) => `
  <div class="${cls(
    "djangd-box",
    padding && "djangd-box--p-" + padding,
    margin  && "djangd-box--m-" + margin,
    display && "djangd-box--" + display,
    align   && "djangd-box--align-" + align,
    justify && "djangd-box--justify-" + justify,
    rounded && "djangd-box--rounded-" + rounded,
    surface && "djangd-box--surface-" + surface
  )}">
    Box content — toggle any modifier in the controls panel.
  </div>`,
};

export const FlexRow = {
  render: () => `
  <div class="djangd-box djangd-box--flex djangd-box--align-center djangd-box--justify-between djangd-box--p-4 djangd-box--surface-variant djangd-box--rounded-md">
    <strong>Left</strong>
    <span>Middle</span>
    <em>Right</em>
  </div>`,
};
