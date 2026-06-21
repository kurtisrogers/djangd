export default { title: "Navigation", tags: ["autodocs"] };

export const AppBar = {
  args: { title: "djangd-framework" },
  render: ({ title }) => `
  <header class="mdc-top-app-bar djangd-app-bar" role="banner">
    <div class="mdc-top-app-bar__row">
      <section class="mdc-top-app-bar__section mdc-top-app-bar__section--align-start" role="toolbar">
        <button class="material-icons mdc-top-app-bar__navigation-icon mdc-icon-button" aria-label="Open menu">menu</button>
        <span class="mdc-top-app-bar__title">${title}</span>
      </section>
      <section class="mdc-top-app-bar__section mdc-top-app-bar__section--align-end" role="toolbar">
        <button class="material-icons mdc-icon-button" aria-label="Search">search</button>
        <button class="material-icons mdc-icon-button" aria-label="Help">help</button>
      </section>
    </div>
  </header>`,
};

export const Tabs = {
  render: () => `
  <div class="mdc-tab-bar djangd-tab-bar" role="tablist" style="max-width:480px;">
    <div class="mdc-tab-scroller"><div class="mdc-tab-scroller__scroll-content" style="display:flex;">
      <button class="mdc-tab mdc-tab--active" role="tab" aria-selected="true" tabindex="0"><span class="mdc-tab__content"><span class="mdc-tab__text-label">Recent</span></span><span class="mdc-tab-indicator mdc-tab-indicator--active"></span></button>
      <button class="mdc-tab" role="tab" aria-selected="false" tabindex="-1"><span class="mdc-tab__content"><span class="mdc-tab__text-label">Starred</span></span><span class="mdc-tab-indicator"></span></button>
      <button class="mdc-tab" role="tab" aria-selected="false" tabindex="-1"><span class="mdc-tab__content"><span class="mdc-tab__text-label">Archive</span></span><span class="mdc-tab-indicator"></span></button>
    </div></div>
  </div>`,
};

export const Breadcrumbs = {
  render: () => `
  <nav class="djangd-breadcrumbs" aria-label="Breadcrumb">
    <ol class="djangd-breadcrumbs__list">
      <li class="djangd-breadcrumbs__item"><a class="djangd-breadcrumbs__link" href="#">Home</a><span class="djangd-breadcrumbs__separator" aria-hidden="true">/</span></li>
      <li class="djangd-breadcrumbs__item"><a class="djangd-breadcrumbs__link" href="#">Library</a><span class="djangd-breadcrumbs__separator" aria-hidden="true">/</span></li>
      <li class="djangd-breadcrumbs__item"><span class="djangd-breadcrumbs__current" aria-current="page">Components</span></li>
    </ol>
  </nav>`,
};
