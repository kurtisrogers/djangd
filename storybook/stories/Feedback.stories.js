export default { title: "Feedback", tags: ["autodocs"] };

export const Alert = {
  args: { severity: "info", title: "Heads up", message: "Your settings have been updated." },
  argTypes: { severity: { control: "select", options: ["info", "success", "warning", "error"] } },
  render: ({ severity, title, message }) => `
  <div class="djangd-alert djangd-alert--${severity}" role="alert" aria-live="polite">
    <i class="material-icons djangd-alert__icon" aria-hidden="true">${
      { info: "info", success: "check_circle", warning: "warning", error: "error" }[severity]
    }</i>
    <div class="djangd-alert__body">
      <div class="djangd-alert__title">${title}</div>
      <div class="djangd-alert__message">${message}</div>
    </div>
  </div>`,
};

export const LinearProgress = {
  render: () => `<div class="djangd-linear-progress mdc-linear-progress mdc-linear-progress--indeterminate" role="progressbar" aria-label="Loading">
    <div class="mdc-linear-progress__primary-bar"><span class="mdc-linear-progress__bar-inner"></span></div></div>`,
};

export const CircularProgress = {
  render: () => `<div class="djangd-circular-progress mdc-circular-progress mdc-circular-progress--indeterminate" role="progressbar" aria-label="Loading">
    <svg viewBox="0 0 48 48"><circle cx="24" cy="24" r="18" fill="none" stroke-width="4" stroke-dasharray="60 60"></circle></svg></div>`,
};

export const Skeleton = {
  render: () => `<div style="max-width:320px;">
    <div class="djangd-skeleton djangd-skeleton--rectangular djangd-skeleton--animation-pulse" style="height:120px;margin-bottom:12px;"></div>
    <div class="djangd-skeleton djangd-skeleton--text djangd-skeleton--animation-pulse">
      <div class="djangd-skeleton__line"></div><div class="djangd-skeleton__line" style="width:80%"></div>
      <div class="djangd-skeleton__line" style="width:60%"></div>
    </div>
  </div>`,
};
