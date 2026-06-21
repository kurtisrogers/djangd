/** @type { import("@storybook/html-vite").StorybookConfig } */
const config = {
  stories: ["../stories/**/*.stories.@(js|mjs|ts)"],
  addons: [
    "@storybook/addon-essentials",
    "@storybook/addon-interactions",
    "@storybook/addon-a11y",
  ],
  framework: { name: "@storybook/html-vite", options: {} },
  staticDirs: ["../public", "../../djangd_framework/static"],
  docs: { autodocs: "tag" },
};
export default config;
