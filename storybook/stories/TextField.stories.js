import { djangoStory, djangoStoryWithControls } from "./_helpers.js";

export default { title: "Inputs/Text Field", tags: ["autodocs"] };

export const Filled   = djangoStory("text_field__filled");
export const Outlined = djangoStory("text_field__outlined");
export const Error    = djangoStory("text_field__error");
export const Textarea = djangoStory("text_field__textarea");

export const Variant = djangoStoryWithControls({
  args: { variant: "filled" },
  argTypes: { variant: { control: { type: "select" }, options: ["filled", "outlined"] } },
  resolve: ({ variant }) => `text_field__${variant}`,
});

export const Select       = djangoStory("select__filled");
export const Autocomplete = djangoStory("autocomplete__default");
export const DatePicker   = djangoStory("date_picker__default");
export const TimePicker   = djangoStory("time_picker__default");
export const ColorPicker  = djangoStory("color_picker__default");
export const NumberField  = djangoStory("number_field__default");
export const Search       = djangoStory("search__default");
export const PasswordField = djangoStory("password_field__default");
export const TagInput     = djangoStory("tag_input__default");
export const InputOtp     = djangoStory("input_otp__default");
export const FileUpload   = djangoStory("file_upload__default");
