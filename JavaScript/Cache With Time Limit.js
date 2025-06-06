class TimeLimitedCache {
    constructor() {
        this.cache = new Map();
    }

    set(key, value, duration) {
        const now = Date.now();
        const hasValid = this.cache.has(key) && this.cache.get(key).expireTime > now;
        this.cache.set(key, {
            value: value,
            expireTime: now + duration
        });
        return hasValid;
    }

    get(key) {
        const now = Date.now();
        if (this.cache.has(key)) {
            const entry = this.cache.get(key);
            if (entry.expireTime > now) {
                return entry.value;
            }
        }
        return -1;
    }

    count() {
        const now = Date.now();
        let cnt = 0;
        for (const entry of this.cache.values()) {
            if (entry.expireTime > now) {
                cnt++;
            }
        }
        return cnt;
    }
}
