import ratelimit from "../config/upstash.js";

const rateLimiter = async (req, res, next) => {
    try {
        // To check success rate
        // "my-rate-limit" <- can provide ip address
        // block based on ip address, not everyone should
        // be blocked if limit exceeds
        const {success} = await ratelimit.limit("my-rate-limit")
        if(!success){
            // 429=To many Request
            return res.status(429).json({message: "To many request, please try again later..."})
        }
        next() // if success then call the function using next()
    } catch (error) {
        console.log("Rate limit Error", error)
        // we can also add error within next
        next(error)
    }
}

export default rateLimiter;