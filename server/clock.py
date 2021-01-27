const clock ={
	template: '#clockFace',
	props: {
	minute: Number,
	tick: Number
	},
	data() {
		return {
			rotation: {
			hours: 0,
			minutes: 0,
			seconds: 0
			}
		}
		},
		computed: {
			hours() {
				return { transform: 'translate3d(-50%, 0, 0) rotate(${this.rotation.hours}deg)'}
		},
		minutes() {
				return { transform: 'translate3d(-50%, 0, 0) rotate(${this.rotation.minutes}deg)'}
		},
		seconds() {
				return { transform: 'translate3d(-50%, 0, 0) rotate(${this.rotation.seconds}deg)'}
				}
		},
		watch: {
			tick() {
			this.rotation.seconds += 6
			this.rotation.minutes += 0.1
			},
			minute(to, from) {
			if (from === to) return;
			this.rotation.hours += 0.5
			}
		},
		mounted() {
			let date = new Date()
			let [h, m, s] = [date.getHours(), date.getMinutes(), date.getSeconds()]
			this.rotation = {
				hours: (h * 30) + (m * 0.5),
				minutes: (m * 6) + (s * 0.1),
				seconds: s * 6,
			}
		},
	}
new Vue({
	el: '#clock',
	components: { clockFace	},
	data() {
	return{
		tick: 0,
		time: { hours: 0, minutes: 0, seconds: 0}
	}
	},
	methods: {
		updateTime(time) {
			this.tick++
			this.time = {
				hours: time.getHours(),
				minutes: time.getMinutes(),
				seconds: time.getSeconds()
			}
			setTimeout(() => this.updateTime(new Date()), 1000 - new Date().getMilliseconds())
		}
	},
	mounted() {
	this.updateTime(new Date())
	}
})
</script>