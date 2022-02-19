# IDOT_pay_items
IDOT pay item data project

The goal of the project is to create a streamlit app that allows users to explory and run machine learning models on data reported by the Illinois Department of Transportation. 
#### Status
- live streamlit app with pay item pricing query
  - users can pick a pay item and see all the records within the past four years and a scatter plot of the unit prices vs quantities

#### Issues
- Some pay items from original data do not show up. Others show up that are not in the original data, per Walter.

#### Work Completed
- Used streamlit cloud to host web app from github repository
- Created working web app to view historical pay item data

#### Work Planned
- Implement machine learning model to predict prices based on pay item and quanity
- Choose pay item by name on the sidebar
- Feature engineering - adding columns to catergorize similar pay items
