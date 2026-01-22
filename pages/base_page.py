class BasePage:
    
    def __init__(self, page, context):
        self.page = page
        self.context = context
    
    @property
    def base_url(self):
        return getattr(self.context, 'base_url', 'https://the-internet.herokuapp.com')
    
    def goto(self, path):
        self.page.goto(f"{self.base_url}{path}")
