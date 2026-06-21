/** @type { import('@storybook/html').Preview } */
import "./preview.css";

const preview = {
  parameters: {
    controls: { matchers: { color: /(background|color)$/i, date: /Date$/i } },
    a11y: { config: { rules: [{ id: "color-contrast", enabled: true }] } },
    docs: { toc: true },
    backgrounds: {
      default: "surface",
      values: [
        { name: "surface", value: "#fffbfe" },
        { name: "dark", value: "#1c1b1f" },
      ],
    },
  },
  globalTypes: {
    theme: {
      name: "Theme",
      description: "djangd-framework theme",
      defaultValue: "light",
      toolbar: {
        icon: "circlehollow",
        items: [
          { value: "light", title: "Light" },
          { value: "dark", title: "Dark" },
        ],
        dynamicTitle: true,
      },
    },
  },
  decorators: [
    (story, context) => {
      document.documentElement.setAttribute(
        "data-djangd-theme",
        context.globals.theme || "light"
      );
      const node = story();
      if (typeof node === "string") {
        const wrap = document.createElement("div");
        wrap.innerHTML = node;
        if (window.djangd) window.djangd.enhance(wrap);
        return wrap;
      }
      return node;
    },
  ],
};
export default preview;
