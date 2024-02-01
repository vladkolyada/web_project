// Partners block variables for animation
const partnersBlock_services = document.querySelector(".partners_block");
const topPositionPartnersBlock_services = partnersBlock_services.offsetTop;

const line_services_partners = document.getElementById("line3");
line_services_partners.style.animationPlayState = "paused";
const smallWords_services_partners = document.getElementById("small_words3");
smallWords_services_partners.style.animationPlayState = "paused";
const bigWords_services_partners = document.getElementById("big_words3");
bigWords_services_partners.style.animationPlayState = "paused";


// Latest News vlock variables for animation
const latestNewsBlock = document.querySelector(".latest_news_block");
const topPositionLatestNewsBlock = latestNewsBlock.offsetTop;

const lineLatestNews = document.getElementById("line_latest_news");
lineLatestNews.style.animationPlayState = "paused";
const smallWords3BB = document.getElementById("small_words3_bb");
smallWords3BB.style.animationPlayState = "paused";
const bigWords3BB = document.getElementById("big_words3_bb");
bigWords3BB.style.animationPlayState = "paused";



function activateAnimationOnBlock (elementAnimation, topPositionClassWithElementAnimation) {
    window.addEventListener('scroll', () => {
        if (window.innerHeight + window.scrollY >= topPositionClassWithElementAnimation) {
          return elementAnimation.style.animationPlayState = "running";
      } else {
          return elementAnimation.style.animationPlayState = "paused";
      }
    });
  }


activateAnimationOnBlock(line_services_partners, topPositionPartnersBlock_services);
activateAnimationOnBlock(smallWords_services_partners, topPositionPartnersBlock_services);
activateAnimationOnBlock(bigWords_services_partners, topPositionPartnersBlock_services);

activateAnimationOnBlock(lineLatestNews, topPositionLatestNewsBlock);
activateAnimationOnBlock(smallWords3BB, topPositionLatestNewsBlock);
activateAnimationOnBlock(bigWords3BB, topPositionLatestNewsBlock);


