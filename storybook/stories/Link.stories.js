import { cls } from "./_helpers.js";

export default { title: "Navigation/Link", tags: ["autodocs"] };

export const Default = {
  args: {
    text: "Read the docs",
    href: "#",
    variant: "body",
    underline: "always",
    color: "primary",
    newTab: false,
  },
  argTypes: {
    text:      { control: "text" },
    href:      { control: "text" },
    variant:   { control: { type: "select" }, options: ["body", "button", "inherit"] },
    underline: { control: { type: "select" }, options: ["always", "hover", "none"] },
    color:     { control: { type: "select" }, options: ["primary", "secondary", "error", "success", "warning", "inherit"] },
    newTab:    { control: "boolean" },
  },
  render: ({ text, href, variant, underline, color, newTab }) => `
  <a class="${cls(
       "djangd-link",
       "djangd-link--" + variant,
       "djangd-link--" + underline,
       "djangd-link--" + color
     )}" href="${href}"
     ${newTab ? `target="_blank" rel="noopener noreferrer"` : ""}>${text}</a>`,
};

export const Button = { ...Default, args: { ...Default.args, variant: "button", underline: "none", text: "Continue →" } };
export const Inline  = {
  render: () => `
  <p style="font-family:var(--djangd-font-family);">
    See the <a class="djangd-link djangd-link--body djangd-link--hover djangd-link--primary" href="#">documentation</a>
    for more details, or contact <a class="djangd-link djangd-link--body djangd-link--always djangd-link--secondary" href="mailto:hi@example.com">support</a>.
  </p>`,
};
