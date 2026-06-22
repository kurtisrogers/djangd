import { djangoStory } from "./_helpers.js";

export default { title: "Feedback", tags: ["autodocs"] };

export const AlertInfo    = djangoStory("alert__info");
export const AlertSuccess = djangoStory("alert__success");
export const AlertWarning = djangoStory("alert__warning");
export const AlertError   = djangoStory("alert__error");
export const Snackbar     = djangoStory("snackbar__default");
export const LinearProgress = djangoStory("linear_progress__indeterminate");
export const CircularProgress = djangoStory("circular_progress__indeterminate");
export const Skeleton       = djangoStory("skeleton__rectangular");
export const EmptyState     = djangoStory("empty_state__default");
