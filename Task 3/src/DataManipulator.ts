import { ServerRespond } from './DataStreamer';

export interface Row {
  price_abc: number,
  price_def: number,
  ratio: number,
  timestamp: Date,
  upper_bound: number,
  lower_bound: number,
  alert_crossing: number | undefined,
}

export class DataManipulator {
  static generateRow(serverRespond: ServerRespond[]): Row {
    const ABC_price=(serverRespond[0].top_ask.price + serverRespond[0].top_bid.price) / 2.0;
    const DEF_price=(serverRespond[1].top_ask.price + serverRespond[1].top_bid.price) / 2.0;

    // calculating ratio
    const ratio = ABC_price / DEF_price ;
    const upper_bound  = 1 + 0.04;
    const lower_bound = 1 - 0.04;

      // returning 1 row at a time
      return {
        price_abc:ABC_price,
        price_def:DEF_price,
        ratio,
        timestamp: serverRespond[0].timestamp > serverRespond[1].timestamp ? serverRespond[0].timestamp : serverRespond[1].timestamp,
        upper_bound,
        lower_bound,
        alert_crossing: (ratio > upper_bound || ratio < lower_bound) ? ratio : undefined,
      };
  }
}
