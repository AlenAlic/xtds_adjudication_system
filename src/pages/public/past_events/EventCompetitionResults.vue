<template>
  <v-card class="fill-height" v-if="!loading">
    <v-card-title class="justify-center">{{ event.name }} ({{ event.date }})</v-card-title>
    <v-card-text>
      <v-card v-if="!!round">
        <v-card-title>
          {{ round.competition.name }}
        </v-card-title>
        <results-expansion-panels
          v-if="changePerRound"
          :round="round"
          :adjudicators="adjudicators"
          :leads="competitors.leads"
          :follows="competitors.follows"
          :competition_listing="competition_listing"
          :evaluation_of_final="evaluation_of_final"
          :ranking_report="ranking_report"
          :mode="round.competition.mode"
        />
        <results-expansion-panels
          v-else-if="changePerDance"
          :round="round"
          :adjudicators="adjudicators"
          :leads="competitors.leads"
          :follows="competitors.follows"
          :competition_listing_leads="competition_listing.leads"
          :competition_listing_follows="competition_listing.follows"
          :evaluation_of_final="evaluation_of_final"
          :ranking_report="ranking_report"
          :mode="round.competition.mode"
        />
        <results-expansion-panels
          v-else
          :round="round"
          :adjudicators="adjudicators"
          :competitors="competitors"
          :competition_listing="competition_listing"
          :evaluation_of_final="evaluation_of_final"
          :ranking_report="ranking_report"
          :mode="round.competition.mode"
          expanded
        />
      </v-card>
    </v-card-text>
  </v-card>
  <loading v-else />
</template>

<script>
import Vue from "vue";
import Loading from "@/components/general/loading/Loading";
import ResultsExpansionPanels from "@/components/public/results/ResultsExpansionPanels";
export default {
  components: {
    ResultsExpansionPanels,
    Loading
  },
  data: function() {
    return {
      loading: false,
      event: null,
      round: null,
      adjudicators: null,
      competitors: null,
      competition_listing: null,
      evaluation_of_final: null,
      ranking_report: null
    };
  },
  created() {
    this.getData();
  },
  computed: {
    singlePartnerModes() {
      return (
        this.round &&
        (this.round.competition.mode === this.$constants.SINGLE_PARTNER ||
          this.round.competition.mode === this.$constants.RANDOM_SINGLE_PARTNER)
      );
    },
    changePerRound() {
      return this.round && this.round.competition.mode === this.$constants.CHANGE_PER_ROUND;
    },
    changePerDance() {
      return this.round && this.round.competition.mode === this.$constants.CHANGE_PER_DANCE;
    }
  },
  methods: {
    getData() {
      this.loading = true;
      Vue.axios
        .get(`event/results/${this.$route.params.event_result_id}`)
        .then(response => {
          const data = response.data.data.result;
          this.event = response.data.event;
          this.round = data.round;
          this.adjudicators = data.adjudicators;
          this.competitors = data.competitors;
          this.competition_listing = data.competition_listing;
          this.evaluation_of_final = data.evaluation_of_final;
          this.ranking_report = data.ranking_report;
        })
        .finally(() => {
          this.loading = false;
        });
    }
  }
};
</script>
