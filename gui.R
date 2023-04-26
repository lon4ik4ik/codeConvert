library(shiny)

# Define the user interface
ui <- fluidPage(
  # Create the input labels and dropdown menus
  sidebarLayout(
    sidebarPanel(
      selectInput(inputId = "product_scope", label = "Product Scope:", choices = c("Cloud - U-Assist", "Cloud - U-Analyze", "Cloud - U-SelfServe", "Cloud - U-Assist + U-Analyze", "Cloud - U-Assist + U-SelfServe", "Cloud - U-Assist + U-SelfServe + U-Analyze", "Cloud - U-Analyze + U-SelfServe", "Prem - U-Assist", "Prem - U-Analyze", "Prem - U-SelfServe", "Prem - U-Assist + U-Analyze", "Prem - U-Assist + U-SelfServe", "Prem - U-Assist + U-SelfServe + U-Analyze", "Prem - U-Analyze + U-SelfServe")),
      selectInput(inputId = "cc_platform", label = "CC Platform:", choices = c("Cisco", "Avaya", "Genesys Cloud", "Genesys PureEngage", "Five9", "inContact", "RingCentral", "Twilio", "Talkdesk", "Amazon Connect", "Other->")),
      selectInput(inputId = "total_level1_call_drivers", label = "Total Level 1 Call Drivers:", choices = c("1-5","6-9", "10-20", "21-30", "31-40", "41-50"))
    ),
    # Create the convert button
    mainPanel(
      actionButton("convert", "Convert")
    )
  )
)

# Define the server logic
server <- function(input, output) {
  # Call the intake.R script with the selected input values as arguments
  observeEvent(input$convert, {
    command <- paste0("Rscript intake.R ", input$product_scope, " ", input$cc_platform, " ", input$total_level1_call_drivers)
    system(command)
  })
}

# Run the application
shinyApp(ui = ui, server = server)
