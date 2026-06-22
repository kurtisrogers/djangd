import { djangoStory, djangoStoryWithControls } from "./_helpers.js";

export default {
  title: "Inputs/Button",
  tags: ["autodocs"],
  parameters: { docs: { source: { language: "django" } } },
};

export const Raised   = djangoStory("button__raised");
export const Outlined = djangoStory("button__outlined");
export const Text     = djangoStory("button__text");
export const Unelevated = djangoStory("button__unelevated");
export const WithIcon = djangoStory("button__with_icon");
export const AsLink   = djangoStory("button__link");
export const Disabled = djangoStory("button__disabled");

export const Size = djangoStoryWithControls({
  args: { size: "medium" },
  argTypes: { size: { control: { type: "select" }, options: ["small", "medium", "large"] } },
  resolve: ({ size }) => `button__${size === "medium" ? "raised" : size}`,
});
