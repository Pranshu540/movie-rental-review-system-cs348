import { TestBed } from '@angular/core/testing';

import { RentalDataService } from './rental-data.service';

describe('RentalDataService', () => {
  let service: RentalDataService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(RentalDataService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
