### **Implementation Plan for Mobile Responsiveness**

This plan outlines the steps to improve the mobile responsiveness of the `app.html` file by modifying `app-styles.css`. The primary goal is to enhance the user experience on smaller screens, particularly mobile devices with a `max-width` of 480px.

#### **1. Add a new media query for smaller mobile devices**
   - Introduce a new media query at `max-width: 480px` in `app-styles.css` to target smaller phones more effectively. This will be the primary breakpoint for the most aggressive mobile optimizations.

#### **2. Refactor Sidebar on small mobile**
   - **Hide sidebar by default:** For screens with `max-width: 480px`, the `.sidebar` element will be set to `display: none;`. This assumes a future implementation of a hamburger menu or similar toggle mechanism to reveal the sidebar.
   - **Adjust `app-shell` grid for hidden sidebar:** Modify the `grid-template-columns` and `grid-template-areas` of `.app-shell` within the `max-width: 480px` media query so that the `main` content takes up the full width, as the sidebar will not be visible.

#### **3. Optimize Topbar elements on small mobile**
   - **Hide non-essential elements:** For `max-width: 480px`, the following elements within the `.topbar` will be hidden to conserve screen space:
     - `.top-search` (the search input and its accompanying '/' span)
     - `.chip` (Cross-margin chip)
     - The "Deposit" and "Withdraw" buttons within the `.wallet-display`.
   - **Condense `wallet-display`:** Adjust the `.wallet-display` to show only the `wallet-address`, potentially truncating it further if needed, and simplify its layout.
   - **Add a placeholder for a menu toggle:** Although the actual JavaScript for a hamburger menu is out of scope for this task, a placeholder element for a menu button will be added to the `.topbar` to indicate where a mobile menu toggle would reside.

#### **4. Improve Main content layout on small mobile**
   - **`portfolio-grid`:** Within the `max-width: 480px` media query, change the `portfolio-grid` to `grid-template-columns: 1fr;` to stack its items vertically, ensuring readability of KPIs.
   - **`markets-header-row` and `market-row`:**
     - For `markets-header-row`, simplify the displayed headers or adjust their font size.
     - For `market-row`, modify its `grid-template-columns` to present essential information more compactly. This might involve stacking elements or making some columns scroll horizontally.
   - **`positions-table`:** For the `.positions-table`, implement a strategy to make it more digestible on small screens. This could involve:
     - Hiding less critical columns (e.g., 'Entry', 'Liq.').
     - Ensuring `overflow-x: auto;` on a wrapper around the table if hiding columns isn't sufficient, to allow horizontal scrolling of the table.
   - **`depth-grid`:** Change the `depth-grid` to `grid-template-columns: 1fr;` to stack its "Bids" and "Asks" columns vertically for better readability.
