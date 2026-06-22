import { djangoStory, djangoStoryWithControls } from "./_helpers.js";

export default { title: "Navigation/Link", tags: ["autodocs"] };

export const Body    = djangoStory("link__body");
export const Button  = djangoStory("link__button");
export const Inherit = djangoStory("link__inherit");

export const Variant = djangoStoryWithControls({
  args: { variant: "body" },
  argTypes: { variant: { control: { type: "select" }, options: ["body", "button", "inherit"] } },
  resolve: ({ variant }) => `link__${variant}`,
});
