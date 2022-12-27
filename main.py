from digitec import scrape as scrapeDigi
from mobileZone import scrape as scrapeMobileZone
from mediamarkt import scrape as scrapeMediaMarkt
from dqSolution import scrape as scrapeDQS
from interdiscount import scrape as scrapeInterdiscount
from computerli import scrape as scrapeComputerli

if __name__ == "__main__":
    scrapeDigi()
    scrapeMobileZone()
    scrapeMediaMarkt()
    scrapeDQS()
    scrapeInterdiscount()
    scrapeComputerli()