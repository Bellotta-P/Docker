import { TestBed } from '@angular/core/testing';

import { VerificheService } from './verifiche.service';

describe('VerificheService', () => {
  let service: VerificheService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(VerificheService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
