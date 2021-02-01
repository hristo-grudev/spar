BOT_NAME = 'spar'

SPIDER_MODULES = ['spar.spiders']
NEWSPIDER_MODULE = 'spar.spiders'
FEED_EXPORT_ENCODING = 'utf-8'
LOG_LEVEL = 'ERROR'
DOWNLOAD_DELAY = 0

ROBOTSTXT_OBEY = True

ITEM_PIPELINES = {
	'spar.pipelines.SparPipeline': 100,

}