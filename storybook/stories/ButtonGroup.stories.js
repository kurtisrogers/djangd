import { djangoStory, djangoStoryWithControls } from "./_helpers.js";

export default { title: "Inputs/Button Group", tags: ["autodocs"] };

export const Horizontal = djangoStory("button_group__horizontal");
export const Vertical   = djangoStory("button_group__vertical");
export const Contained  = djangoStory("button_group__contained");

export const Variants = djangoStoryWithControls({
  args: { orientation: "horizontal", variant: "outlined" },
  argTypes: {
    orientation: { control: { type: "select" }, options: ["horizontal", "vertical"] },
    variant:     { control: { type: "select" }, options: ["outlined", "contained"] },
  },
  resolve: ({ orientation, variant }) => {
    if (variant === "contained") return "button_group__contained";
    return `button_group__${orientation}`;
  },
});
