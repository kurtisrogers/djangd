const render = ({ outlined, title, body, media }) => `
<div class="mdc-card djangd-card ${outlined ? "mdc-card--outlined" : ""}" style="max-width:360px;">
  ${media ? `<div class="mdc-card__media" style="background-image:url('${media}');" role="img" aria-label="Hero image"></div>` : ""}
  <div class="mdc-card__content">
    <h2 class="mdc-typography mdc-typography--title-large djangd-typography djangd-typography--title-large" style="margin:0 0 8px;">${title}</h2>
    <p class="mdc-typography mdc-typography--body2 djangd-typography djangd-typography--body-medium" style="margin:0; color: var(--djangd-color-on-surface-variant);">${body}</p>
  </div>
  <div class="mdc-card__actions">
    <button class="mdc-button djangd-button">Cancel</button>
    <button class="mdc-button mdc-button--raised djangd-button djangd-button--raised">Confirm</button>
  </div>
</div>`;

export default {
  title: "Surfaces/Card",
  tags: ["autodocs"],
  render,
  argTypes: {
    outlined: { control: "boolean" },
    media:    { control: "text" },
    title:    { control: "text" },
    body:     { control: "text" },
  },
  args: {
    outlined: false,
    media: "https://placehold.co/720x405/eaddff/21005d.png?text=djangd",
    title: "Material card",
    body:  "Cards contain content and actions about a single subject.",
  },
};
export const Elevated = {};
export const Outlined = { args: { outlined: true } };
export const NoMedia  = { args: { media: "" } };
