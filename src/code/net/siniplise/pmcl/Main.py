import net.siniplise.pmcl.model.Application_Initialization as Application_Initialization
import net.siniplise.pmcl.model.Loging as log4j

cache_dir = '..\\..\\..\\..\\..\\run\\.pmcl'
log4j.main_logger.info("Connect Logger Successful")

Application_Initialization.app_init(cachedir='..\\..\\..\\..\\..\\run\\.pmcl')

# class Main:
#     def __init__(self):
#         pass
#
